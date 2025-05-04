# Facebook Privacy Settings

## Functional Req
- Users can change privacy settings for posts (Public → Friends → Only Me → Custom Lists)
- Changes must reflect immediately for the post owner
- Changes should propagate to all feeds and caches (< 2sec)
- Users can define custom friend lists for granular sharing
  
## Non-Functional Req
- Latency: <500ms for owner, <5s for other users
- Consistency: Strong for the owner, eventual for others
- Scalability: Handle 1 M+ privacy changes/second
- Availability: 99.99% uptime (partial failures shouldn't block updates)
- Durability: No lost privacy updates

## Scale Estimates
  - 500M DAU, 100M privacy changes/day
  - Peak: 50K updates/second
  - Storage:
    100B posts × 1KB metadata = 100TB metadata

## Entities
  - User, Privacy, Post, Friend 

## High-level Design
```
flowchart TD
    A[Client] --> B[API Gateway]
    B --> C[Privacy Service]
    C --> D[Content DB]
    C --> E[TAO]
    C --> F[Kafka]
    F --> G[Feed Service]
    F --> H[Search]
    F --> I[Notifications]
    G --> J[Feed DB]
    H --> K[Elasticsearch]
```

## Deep Dives

### How to remove a post from millions of precomputed feeds?
  - The change is updated in Privacy settings DB
  - and the change ins added to Kafka queue
  - From Kafka it will be sent to
    - TAO(graph DB)
    - Feed Update Service
    - Post DB.updet teh DB with "HIDDEN"
  - Feed update service will update the Feed table with the privacy setting, updet posts to "HIDDEN"
  - It can be sequential or batch
  - hot user:
    - if we don't follow async(kafka) approach for hot user then update the post
    - or else we update the feed table

### Privacy Settings Storage Architecture
