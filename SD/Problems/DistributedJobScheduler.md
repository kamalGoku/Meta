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
- `time_bucket` will give the next hour tasks, and `execution_time` will give the exact time to execute them
- This makes the query easier to look at 1-2 buckets

### 2) Users should be able to monitor the status of their jobs
- Querying for the jobs by userId needs to look up the  jobs table and the execution table
- So have a *Global Secondary Index* as `userId` in Execution Table, which makes the queries faster

# Deep Dives
