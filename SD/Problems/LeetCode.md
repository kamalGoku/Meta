# High-Level Design
### 1) Users should be able to view a list of coding problems
  - User to Server to DB, query problems
  - Problem with having id, title, description, code sub, testcases

### 2) Users should be able to view a given problem and code a solution
 - User queries the problem with problemId, a code stub for that problem is given

### 3) Users should be able to submit their solution and get instant feedback
  - Running code on the Server will crash the server
  - Running on VM: not cost-effective and cold-start
  - Running on Containers(Docker): More effective than VM, a container for each language, store the submission in the submission DB and return the result to the user
  - Running on a Serverless function: Similar to a Container

### 4) Users should be able to view a live leaderboard for competitions
  - Create a competition, with a max time of 90min, 4 problems, max users 100k
  - User queries the DB every 5 seconds with the competitionId as key, checks all submissions and groups by userId

# Deep Dives
### 1) How will the system support isolation and security when running user code?
  - Have a read-only file system
  - CPU and memory bounds
  - have timeouts (max 5 sec)
  - Use VPC, no network calls
  - No system calls

### 2) How would you make fetching the leaderboard more efficient?
  - Use Redis, which caches submissions. Poll the DB every 20 seconds and update the cache, but this approach is not real-time
  - Use Redis Sorted Set, which polls periodically and sorts the score
    - Every submission will update the DB and also the Redis cache
    - ZADD to add to the Redis cache
    - ZREVRANGE to get the leaderboard for the top N users
    - Client polls every 5 seconds is very fast
    - The polling time can be increased at the end
   
### 3) How would the system scale to support competitions with 100,000 users?
  - Have Dynamic Horizontal scaling with Elastic Container Service(ECS), which scales based on users, but not cost-effective
  - Use Amazon SQS for queuing the submission to the containers
  - The worker will take the job from SQS and submit it to the container, and return the result to the Service
  - Having SQS will also help in resubmission in container failure
  - This makes the submission asynchronous, and hence we can have an endpoint as /check which polls for results from the server.

### 4) How would the system handle running test cases?
  - Use one test case for all languages, serialise it, deserialise while running
