# Facebook Post Search

## Functional Req

- Users should be able to create posts and like posts
- Users should be able to search posts by keyword
- Users should be able to get the results sorted by recency or num of likes

## Non-Functional Req

- Search must be fast < 500ms
- Support high volume of requests
- New post should be searchable < 1min
- Old posts should be searchable(with a delay)
- Highly available

## High-Level Design

### 1) Users should be able to create and like posts.
- Post Service to Ingestion Service to Index
- Like Service to ingestion Service to Index

### 2) Users should be able to search posts by keyword.
- Client to Search Service via an API Gateway to Index
- Indexing the DB with a keyword is BruteForce, so create a Redis cache with "Inverted Index" from the DB 
- Inverted index stores the keyword to a list of posts mapping. Ingestion service tokenises the input post and updates the keyword mapping
  
### 3) Users should be able to get search results sorted by recency or like count.
- Querying and sorting will be very slow
- Store two Index, one sorted by likes and the other sorted by time
- Redis has "Sorted lists" which store in sorted order. Whenever a new post is created, the Index is updated
- Queries are faster, but the cost to store(DB) is high

## Deep Dives

### 1) How can we handle the large volume of requests from users?
- 2 req: no personalisation, posts available in 1 min
- Good Sol: use Distributed Cache with 1 min TTL
- Great Sol: Use CDN before Search Service

### 2) How can we handle multi-keyword, phrase queries?
- Good Sol: Query keywords and Intersection, but the query takes time
- Great Sol: Bigrams/Shingles: Store two keywords as an Index
- Use Bigrams and fallback to the intersection if the keyword is not found

### 3) How can we address the large volume of writes?
- Post Creation:
  - Ingestion service will be overwhelmed with requests, so have a log/stream service, Kafka, before that.
- Like Event:
  - batch processing of likes
  - Good Sol: Batch of 100 likes. But useful only for popular posts. also latency
  - Great Sol: Batch processing in power of 2, e.g. 2,4,8 etc, but even that is not sufficient
               During user query, get the latest from Like Service (Two Stage Architecture)
    
### 4) How can we optimise the storage of our system?
- move old posts to S3
