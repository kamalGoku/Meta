## Task: "send an email"
## Job: "send an email" at 10.30 AM every Friday

# Functional Req
- Schedule jobs
- Monitor the status of the job
  
# Non-Functional Req
- Ask about the scale of the system
- 10k jobs/s
- execute within 2s
- availability >> consistency
- at least once execution model

# API
```
POST /jobs
{
  "task_id": "send_email",
  "schedule": "0 10 * * *",
  "parameters": {
    "to": "john@example.com",
    "subject": "Daily Report"
  }
}
```

```GET /jobs?user_id={user_id}&status={status}&start_time={start_time}&end_time={end_time} -> Job[]```

# High-Level Design

### 1) Users should be able to schedule jobs to be executed immediately, at a future date, or on a recurring schedule
- User submits task to /jobs endpoint
- If we have a job and its execution time in the same table, then querying the next executable jobs will not be efficient
- so have 'jobs' table and 'execution' tables
- execution table stores `time bucket` as the partition key, `timebucket = time//3600`, and status as `PENDING`
- JOB table
```
{
  "job_id": "123e4567-e89b-12d3-a456-426614174000",  // Partition key for easy lookup by job_id
  "user_id": "user_123", 
  "task_id": "send_email",
  "schedule": {
    "type": "CRON" | "DATE" 
    "expression": "0 10 * * *"  // Every day at 10:00 AM for CRON, specific date for DATE
  },
  "parameters": {
    "to": "john@example.com",
    "subject": "Daily Report"
  }
```
- EXECUTION Table
```
{
  "time_bucket": 1715547600,  // Partition key (Unix timestamp rounded down to hour)
  "execution_time": "1715548800-123e4567-e89b-12d3-a456-426614174000",  // Sort key (exact execution time and the jobId since partition key and sort key must be unique)
  "job_id": "123e4567-e89b-12d3-a456-426614174000",
  "user_id": "user_123", 
  "status": "PENDING",
  "attempt": 0
}
```
- *partition-key* = user-id
- *sort-key* = execution-time
- `time_bucket` will give the next hour tasks, and `execution_time` will give the exact time to execute them
- This makes the query easier to look at 1-2 buckets

### 2) Users should be able to monitor the status of their jobs
- Querying for the jobs by userId needs to look up the  jobs table and the execution table
- So have a *Global Secondary Index (GSI)* as `userId` in Execution Table, which makes the queries faster

# Deep Dives
### 1) How can we ensure the system executes jobs within 2 seconds of their scheduled time?
- Querying the main DB every 2s will have 20k operations is heavy and can cause schedule delay, performance impact
- We need to poll the DB every 5 minutes and get the next execution jobs and put them in a Message queue, workers will take from the queue and execute
- This 5-minute extra delay will give extra buffer, but the queue is still FIFO; you need a priority queue
- Message Queue:
  - Rabbit MQ as Message Queue - it is good, but doesn't support message delay, natively, rather with a plugin, doesn't have retries
  - Amazon SQS - has delayed message functionality and also has retries
  
### 2) How can we ensure the system can support up to 10k jobs per second?
- Scalability for all modules - go from left to right
- Job Creation:
  - is one-time job >> recurring, then we have more writes
  - Better to have a Kafka or Rabbitmq for handling the surge of schedule requests.
- DB:
  - Tables are already partitioned with partition keys, and Cassandra or Dynamodb will easily scale
  - These Databases support a million writes/s
- Message Queue:
  - 10k/s * 300 sec = 30000000 (3M) messages in 5 minutes, each 200KB in size
  - SQS takes care of the scale and sharding automatically
- Workers:
  - Containers: Cost-effective, but don't scale automatically
  - Lambda: short-lived and scalable automatically, but cold start
  - Better to go with Containers with ECS as it is cost-effective
    
### 3) How can we ensure at least once execution of jobs?
- Visible Failures: having errors in logs from worker execution
- Invisible Failures: Worker failures
- Handle Worker Failure:
  - Job Lease: Mark the DB as Worker A is executing, so another worker will not take the job and retry if it fails
  - SQS: SQS makes the job invisible if assigned to the worker, and if it fails, it will release the visibility
- Handle idempotency:
  - Have a deduplication table
  - Create idempotent tasks
