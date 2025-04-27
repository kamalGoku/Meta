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
  - The videos will be consumed by the Kafka Queue 
