## 🧠 Redis – Interview Cheat Sheet

### 🔷 What is Redis?
- **Redis** = Remote Dictionary Server  
- **In-memory**, **key-value** data store  
- **Single-threaded**, extremely **fast and predictable latency**  
- Often used for **caching**, **real-time analytics**, **queues**, **leaderboards**, etc.
- written in C

---

### 🔧 Core Features

| Feature            | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **In-memory**      | All operations are done in memory → very fast                              |
| **Data Structures**| Strings, Hashes, Lists, Sets, Sorted Sets, Bitmaps, HyperLogLogs, Streams  |
| **Atomic ops**     | All Redis operations are atomic due to the single-threaded model           |
| **Pub/Sub**        | Messaging pattern – enables real-time event processing                     |
| **Streams**        | Log-like structure → similar to Kafka-style messaging                      |
| **TTL support**    | Native key expiration → great for caches                                   |

---

### 🗃️ Data Structures (with use-cases)

| Data Structure | Use Case                             |
|----------------|---------------------------------------|
| **String**     | Counters, tokens                     |
| **Hash**       | Object storage (e.g., user profile)  |
| **List**       | Queues, recent activity logs         |
| **Set**        | Unique tags, items                   |
| **Sorted Set** | Leaderboards, ranking with scores    |
| **Stream**     | Event queues, messaging pipelines    |

---

### ⚙️ Redis in Production

#### 💡 Deployment Modes
- **Single Node** – simple, fast
- **Master-Slave (Replication)** – for **high availability** (read replicas)
- **Sentinel** – automatic failover management
- **Cluster Mode** – for **horizontal scalability**

#### 🔗 Cluster Mode
- Uses **hash slots (0-16383)** to partition data
- Clients **cache slot-node mapping** to route requests
- Nodes use a **gossip protocol** to sync and detect failures

---

### 🧱 Durability & Persistence

| Mode         | Description                                           |
|--------------|-------------------------------------------------------|
| **AOF**      | Append Only File → logs all write operations          |
| **RDB**      | Point-in-time snapshots at intervals                  |
| **Hybrid**   | Use both AOF + RDB for balance                        |
| **Tradeoff** | More durability = slower; Redis prioritizes speed     |

#### ✅ For stronger durability:
- Use **Redis on Flash** or **AWS MemoryDB** (slower but disk-backed)

---

### ⚠️ Trade-offs

| Strengths                     | Limitations                           |
|------------------------------|----------------------------------------|
| Ultra-fast                   | Data loss possible if not persisted   |
| Rich data structures         | Memory-bound – limited by RAM         |
| Simple setup & operations    | Single-threaded – may bottleneck CPU  |
| Built-in replication & failover | Complex consistency in clusters    |

---

### 📌 Redis in System Design Interviews

Use Redis for:
- **Caching** (e.g., DB query results, sessions)
- **Rate limiting** (using INCR & TTL)
- **Queues & Pub/Sub** (notifications, jobs)
- **Leaderboards** (Sorted Sets)
- **Locks** (simple distributed locking with SETNX)

---

## 🔁 Final Tips for Interviews

- **Use TTL** to auto-expire keys (great for caches/sessions)
- **Mention AOF + RDB** for durability trade-offs
- **Describe cluster using hash slots + client routing**
- **Explain data structure fit for use-case**
- **Always highlight trade-offs**: speed vs durability, memory usage vs performance
