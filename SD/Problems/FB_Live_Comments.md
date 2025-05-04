
## Functional Req:
  - Users can post comments on live video
  - Users can see new comments posted on the video
  - Users can see comments made before joining the live video

## Non-Functional Req:
  - scale supports millions of videos, 1000+ comments/s per video
  - availability > consistency, eventual consistency
  - low latency, broadcast in near-realtime (~200ms)

## Entities:
  - Users
  - Live Video
  - Comments
 
## API & System Interface
```
  - POST /comments/:liveVideoId
    Header: JWT | SessionToken
    {
        "message": "Cool video!"
    } 
  - GET /comments/:liveVideoId?cursor={last_comment_id}&pageSize=10&sort=desc
```

## High-level Design:

### 1) Viewers can post comments on a Live video feed
  - User-->Comment Mgmt Service---> DB
  - DB is made as Cassandra? Because it is highly available, and storing comments doesn't require relationships
  - Comment DB:
    - commentId(PK), videoId, content, author, createdAt 
    
### 2) Viewers can see new comments posted while watching the live video.
  - Poll the DB every few ms(for real-time) with the 'since last commientId'
  - gives lots of stress to DB

### 3) Viewers can see comments made before they joined the live feed  
  - Query the DB with offset and get the comments list in multiple pages.
  - Pagination: break a large set into small chunks
  - Bad Sol: use offset pagination, 'offset=0', this has to count through all comments preceding the offset in the DB
  - Good Sol: use cursor pagination: 'cursor=lastCommentId' and it gets updated in every fetch, more efficient if DB is built with the same key.
    Even if a comment is deleted, the cursor pagination will work.

## Deep Dives:

### How can we ensure comments are broadcast to viewers in real-time?
  - HTTP polling will be slow and not real-time, so Websockets vs SSE,
  - Websockets: 2-way comm, write comments and read comments are not balanced, so this is not a good approach, uses its own protocol and not HTTP,
  - SSE is the best as the comments read >>> writes, use HTTP post for comment write
    Challenges: Browsers impose a  max number of SSE connections, and LB can terminate SSES

### How will the system scale to support millions of concurrent viewers?
  - Have separate Realtime Comment Management Service for fetching comments(read) and Comment Service for handling comment writing(write)
  - Millions of SSE have to scale with multiple Realtime Comment Services
  - Bad Sol: Having a pub/Sub (Redis) so that Realtime Comment Services will listen to that sub and update the connection mapping
  - Good Sol: Having pub/sub partitioned by videoId, having a has(videoId)%N channels, the Realtime Comment Services will read only the videoId associated with it
  - Great Sol: pub/sub with Layer 7 LB, the server will subscribe only to the videoId that the users connected to it are watching, you can use Zookeeper to do the mapping, Kafka pub/sub vs Redis pub/sub?
  - Great Sol: Use the Dispatcher, which directly maps the Realtime Comment Service

- Redis Pub/Sub - low latency, but don't store the message
- Kafka Pub/sub - high latency, but stores the message, persistent
