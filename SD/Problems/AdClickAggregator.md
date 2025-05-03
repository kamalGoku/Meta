## Function Req
  - Users can click on an ad and be redirected to the advertiser's website
  - Advertisers can query ad click metrics over time with a minimum granularity of 1 minute

## Non-Functional Req
  - ask about the scale, like 10M AU and 10K clicks/sec

## System Interface
 - input: Ad click metrics from users
 - Output: Ad click metrics for advertisers

## Data Flow

## HLD

### 1) Users can click on ads and be redirected to the target
  - user, ad placement service and Click Processing Service
  - Good Sol: putting the redirect URL in the click, we can't track the metrics, users can bypass
  - Great Sol: Click will come to the server, and we will give the redirect URL. downside: user exp

### 2) Advertisers can query ad click metrics over time at 1-minute intervals
  - Bad Sol: Store the clicks in DB(eventId, adId, userId) and query the DB with GROUP_BY command, Downside: very poor perf at this scale
  - Good Sol: Having seprate analytics DB
    - Schema: AdId, TS, Clicks
    - Click events are capured in DB(Cassandra), why cassandra? because write heavy
    - Run a Dist Computing Engine(Apache Spark) every 5 min on this DB
    - 10k click/sec ---> 60*10k * 5 ~ 3M click/min - 300MB/min of data, which Spark can handle
    - Using Map-Reduce Spark aggregates (adId, clicks) data to OLAP DB (Redshift)
    - Downside:
      - If the scale of clicks increases, then the DB can't handle
      - Not real-time, as we run a 5-minute Cron job for aggregation
  
 - Great Sol: Stream processing
   - Clicks are captured by Kafka and processed by Flink
   - Kafka/Kinesis - even streams
   - Flink: Stream processing service
   - Once the configured window is reached, Flink writes to the OLAP DB
   - Challenges:
     - Same as the spark approach, but we can configure the granularity window here.
     - Flink can have minute-level granularity.

## Deep Dives

### 1) How can we scale to support 10k clicks per second?
  Scaling: go left to right
  - Have horizontal scaling (use LB)
    - Click processing Service
    - Kafka/Kinesis: shard by adId, each shard can handle 1000 req/s
    - Flink: Flink can be scaled, and each adId can be processed by one Flink
    - OLAP: shard by adId
  - Hot shards
    - Distribute hot AdId to different shards with a random number(0...N), additional partitions required for AdId.
    - In this way, the throttling is secured, but we need to adjust Flink to ignore this random number during agg.
  
### 2) How can we ensure that we don't lose any click data?
  - Kinesis/Kafka is already distributed, and hence they are highly available, fault-tolerant
  - 7-day retention period for Kinesis/Kafka ensures data is there
  - Having a Checkpoint is not a good solution, as we are aggregating every minute
  - We can store the raw click events in S3 and run Spark on that data every hour/day. Reconcile the batch process output to OLAP.
  - This hybrid method of Kinesis + Spark ensures the analytics are fast and correct
  - 
### 3) How can we prevent abuse from users clicking on ads multiple times?
    - AdPlacement Service generates all with an impression ID
    - When a user clicks the ad, the click data is sent with the impression ID.
    - Click service checks the signature of the impression ID, and if valid, it puts it in the Redis cache
    - If the impression ID is already present, then the click is not added to Kinesis, else we do
    - We are having the fingerprint here to check if any malicious user is mimicking the impression ID.
    - The cache can be scaled and is fault-tolerant

### 4) How can we ensure that advertisers can query metrics at low latency
    - We use OLAP, which aggregates the data
    - We can run a Cron job which aggregates for days, months and years for fast access
