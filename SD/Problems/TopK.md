# TOP K videos/any

https://medium.com/@techturtles51/system-design-interview-top-k-heavy-hitters-ab49640f3ec9

## Functional Req
- Users should query the top K videos
- Periods should be limited to 1 hour, 1 day, 1 month

## Non-Functional Req
- Highly scalable: scale for massive amounts of events
- Highly Available: uninterrupted access to collect trending data
- High performance - low latency; return in 10s of milliseconds
- Results must to precise

## Scale Estimation
- 70B views/day / 100K seconds/day = 700K views/sec


## High-Level Design
- Simple architecture:
  - Calculate from the incoming stream to a Heap and a HashMap.
  - Store the results in the DB after the time window
  - Pros: Fast, as it's in-memory
  - Cons: Not scalable
- Horizontal Scaling
  - Scale the Hashmap+MinHeap Server
  - Shard the Server based on event-id/video-id.
  - Aggregate from the servers and store in the DB
  - Not scalable, fails with the increase in videos
- Count-Min Sketch and Minheap
  - In memory Count-min sketch algorithm
  - Results are realtime(fast) but approximate
  - Doesn't need to scale with an increase in videos, as it's fixed memory
  - Cons: Not precise
- File Storage + MapReduce Jobs
  - Give precise results
  - The videos will be consumed by the Kafka Queue and saved in HDFS
  - Run MapReduce(Apache MapReduce) jobs on the HDFS data every 1 hour
    - One job aggregates data based on video ID
    - The second job calculates the top K video IDS
  - Every hour, the data will be stored in the DB

## Deep Dive

- Final solution to combine the fast and slow approaches.
- 2 paths of data processing from Kafka, one to Count-min sketch and another to File Storage + MapReduce
- Bottlenecks to Solve:
  - Kafka Bottleneck: Partition by videoId for better scaling
  - CMS: have multiple hash functions for better accuracy, uses SpaceSaving algorithms
  - HotKey issue:
    - Salting the key and distribute in Kafka
    - restore in the key during mapReduce
