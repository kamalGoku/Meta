# Facebook Newsfeed

## Function Req
- Users should be able to create posts
- Users should be able to friend/follow other users
- Users should be able to view posts from friends/followers in chronological order
- Users should be able to scroll through the new feed

## Non-Functional Req
- Highly available. Tolerating 2 min of eventual consistency
- Posting and viewing should be fast <500ms
- The system should handle the massive number of users(2B)
- Users can follow/followed by an unlimited number of users

## Enitities
  - User, Follow, Post

## API
```
  - POST /post
    Request:
    {
        "content": {
    
        }
    }
    Response:
    {
        "postId": // ...
    }
  - POST /user/[id]/followers
    Request: 
    {
    
    }
  - GET /feed
    Response: 
    {
        items: POST[]
    }
```
## High-Level Design
### 1) Users should be able to create posts.
- Post Service and Post Table

### 2) Users should be able to friend/follow people.
- Friends Service and Follow Table
- Friends DB have the mapping of users, user1:user2

### 3) Users should be able to view a feed of posts from people they follow.
- Feed Service, accessing the Follow Table and Post Table
- Partition the Post table by userid for fast access
  
### 4) Users should be able to page through their feed.
- Feed service access a Cache(Redis) which stores list of recently viewed post with TTL <1min
- The Feed service will fetch from the last shown timestamp

## Deep Dives
### 1) How do we handle users who are following many users?
- Bad Sol: Horizontal scaling with sharding.
- Have a 'Precomputed' Feed Table. Store the posts' IDS for the users.
- Update this table whenever a new post is created.
- Instead of fetching from the Follow Table and Posts Table, they can query from here, which makes it faster.

### 2) How do we handle users with many followers?
- Bad Sol: Shotgun the requests. Write to feed when a new post is created
- Great Sol:
  - Have an Async worker queue(Amazon SQS), Post service writes to this queue. Async worker will write to the Feed Table and the Posts Table.
  - Since the tolerable limit is <2sec, this will work
  - Downside: Users with large numbers of followers need lots of workers to write to millions of entries.
- Great Sol:
  - Users with large followers will not be written to the async workers.
  - The posts will be fetched from the table directly and merged from the async worker output.
  - Hybrid approach of Queue & non-queue
  
### 3) How can we handle uneven reads of Posts?
- One post with millions of reads and another post with 100s of reads
- Good Sol: Post cache with Large keyspace. Have a Redis cache between the Feed service and the Posts Table
- Great Sol: Hot partition problem. Have multiple instances of Cache and distrubte among them
