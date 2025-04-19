# Facebook Privacy Settings - Full System Design (Staff-Level)

---

## Table of Contents
1. Problem Statement
2. Requirements
3. Non-Functional Requirements
4. Core Challenges
5. High-Level Architecture
6. Data Modeling
7. Privacy Access Control Engine
8. Caching Strategy
9. Consistency & Freshness
10. Security & Abuse Prevention
11. Extensibility
12. Trade-offs
13. Operational Considerations
14. Diagrams
15. Mock Interview Q&A

---

## 1. Problem Statement
Design a privacy settings system for a social media platform like Facebook, enabling users to control who can access their content (posts, photos, profiles, etc.) with high granularity and scalability.

---

## 2. Requirements

### Functional Requirements
- Users can define privacy settings at both global and per-entity levels.
- Support privacy levels: `PUBLIC`, `FRIENDS`, `FRIENDS_OF_FRIENDS`, `ONLY_ME`, `CUSTOM`.
- Allow defining and managing friend lists.
- Support blocking and restricted access.
- Privacy settings should apply in real-time or near real-time.

### Use Cases
- User posts content with default settings.
- User overrides post visibility.
- Viewer requests access to content and system evaluates permissions.

---

## 3. Non-Functional Requirements
- High availability (99.99%)
- Low latency access checks (<100ms)
- Horizontal scalability
- Eventual consistency acceptable for reads; strong consistency for writes
- Auditability and traceability

---

## 4. Core Challenges
- Expressive access policies
- Highly dynamic social graph
- Low-latency enforcement at massive scale
- Managing precomputation vs real-time evaluation

---

## 5. High-Level Architecture
```
+----------------------+      +---------------------+
|     Client App       |<---->|     API Gateway     |
+----------------------+      +---------------------+
                                    |
               +------------------------------------------+
               |     Privacy Settings Service             |
               +------------------+-----------------------+
                                  |
                                  v
                     +---------------------------+
                     |     ACL Computation       |
                     +---------------------------+
                                  |
                                  v
                +------------------------------------------+
                |      Denormalized ACL Store (KV/Doc)     |
                +------------------+-----------------------+
                                  |
                        +---------v----------+
                        |   Caching Layer     |
                        +---------------------+
                                  |
                        +---------v----------+
                        |    Content Store    |
                        +---------------------+
```

---

## 6. Data Modeling

### User
```sql
User(user_id, name, email, created_at)
```

### Privacy Setting
```sql
PrivacySetting(
  id UUID,
  user_id,
  entity_type ENUM('post', 'photo', 'profile'),
  entity_id,
  visibility ENUM('PUBLIC', 'FRIENDS', 'FOF', 'ONLY_ME', 'CUSTOM'),
  allow_list_id UUID,
  deny_list_id UUID,
  created_at,
  updated_at
)
```

### Friend List
```sql
FriendList(list_id UUID, user_id, name)
FriendListMembership(list_id UUID, friend_id UUID)
```

### Block List
```sql
BlockList(user_id, blocked_user_id)
```

### ACL Store
```json
Key: acl:post:{post_id}
Value: {
  "owner_id": "user123",
  "visibility": "CUSTOM",
  "allowed_user_ids": ["u1", "u2"],
  "denied_user_ids": ["u3"]
}
```

---

## 7. Privacy Access Control Engine

### Evaluation Steps:
1. Retrieve entity ACL from cache or KV store.
2. If `PUBLIC`, allow.
3. If `ONLY_ME`, allow only owner.
4. If `FRIENDS`, check friendship.
5. If `FOF`, perform 2-hop graph traversal.
6. If `CUSTOM`, match against allow/deny lists.
7. Check block list for both directions.

### Design Considerations:
- Cache ACLs for hot content.
- Precompute `PostACL(user_id, post_id)` for fast lookup.
- Use graph DB or adjacency lists for FOAF.

---

## 8. Caching Strategy
- Use Redis for hot ACLs (TTL-based + event-driven invalidation).
- Use Bloom Filters for large list membership.
- Background job to refresh stale caches.

---

## 9. Consistency & Freshness

| Component        | Consistency     | Rationale                        |
|------------------|------------------|----------------------------------|
| Settings writes  | Strong           | Must immediately reflect change |
| ACL cache        | Eventual         | Async updates acceptable        |
| Friendship graph | Eventual         | Acceptable delay in FOAF logic  |

Tools:
- Kafka or Pulsar for propagating updates
- Zookeeper/Consul for leader election and failover

---

## 10. Security & Abuse Prevention
- Rate limit privacy changes
- Log access evaluations
- Encrypt sensitive fields
- Protect against abuse via rapid visibility toggle

---

## 11. Extensibility
- Add new visibility levels: e.g., geography-based, age-restricted
- Pluggable rule engine (e.g., DSL or policy engine like Zanzibar)
- Support for Stories, Reels, future content types

---

## 12. Trade-offs

| Option | Pros | Cons |
|--------|------|------|
| Precompute ACLs | Fast read | High write/load cost |
| Real-time evaluation | Dynamic | Latency, complexity |
| Graph DB | Flexible | Costly traversal |
| Redis cache | Fast | Invalidation complexity |

---

## 13. Operational Considerations
- Health checks and dashboards for ACL computation jobs
- Dead-letter queues for failed updates
- Backfill tools for rebuilding ACLs
- Dark launches for new privacy rules
- Canary deployments

---

## 14. Diagrams
_(To be attached: Component diagram, sequence flow of post creation and privacy check, data flow for ACL build)_

---

## 15. Mock Interview Q&A

**Q: How would you support visibility like "Friends except some people"?**
> Add a `deny_list_id` to the privacy setting and apply it during access evaluation.

**Q: What happens when a user unfriends someone?**
> Trigger an event, recompute any ACLs involving that user, and update caches.

**Q: How would you handle a user with 10M friends?**
> Use lazy evaluation, sharded friend lists, and Bloom filters for membership checks.

**Q: How do you ensure privacy changes are fast?**
> Use strong consistency on writes, async propagation to ACL cache, and real-time invalidation on hot content.

**Q: What are the biggest failure points?**
> - ACL builder failures
> - Event stream lag
> - Stale caches
> Implement alerts, retries, and backfills for each.

---

> This design ensures high scalability, flexibility in policy enforcement, low-latency reads, and strong control for users over their content.

---

