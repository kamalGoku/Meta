# ONLINE AUCTION

## High-Level Design

### 1) Users should be able to post an item for auction with a starting price and end date.
- Auction Service (/auction endpoint) and DB
- Auction Table:
  - auctionId, itemId, startTime, endTime, creatorId
- Item Table:
  - itemId, itemName, description

### 2) Users should be able to bid on an item. Bids that are higher than the current highest bid are accepted.
- Bidding Service and DB
- Bid Table
  - bidId, auctionId, price, userId

### 3) Users should be able to view an auction, including the current highest bid.
- Auction Service will fetch the details with /auction/:auctionId

## Deep Dives 

### 1) How can we ensure strong consistency for bids?
- Good Sol: Having Redis cache:
  - stores the current highest bid
  - but created a problem of sync DB and cache, extra check
- Great Sol: Lock only one auction row
  - only one row is locked, checked for max val and commit
  - can have OCC also (optional)

### 2) How can we ensure the system is fault-tolerant and durable?
- Message queue between the Gateway and the Bidding Service
  - The bid is not lost, stored in queue
  - Buffering in a heavy load scenario
  - Ordering is guaranteed
- Use Kafka for a Message queue
  - durable, partitioning based on auctionId
### 3) How can we ensure the system displays the current highest bid in real-time?
- Client polling will not be real-time
- Have SSE notify to clients to notify the highest bidder
- Websockets are also OK
- Challenge: mapping of user sessions in the auction service

### 4) How can we ensure the system scales to support 10M concurrent auctions?
- Left to right
- 10M concurrent auctions, 1B / 100,000 (rounded seconds in day) = 10K bids per second.
- Message Queue:
  - Kafka is scalable
- Bidding Service
  - Horizontal scaling
- DB:
  - approx 25TB per year of storage needed
  - shard based on auctionId for better read/write
- SSE:
  - Have a pub/sub model among the bid services to know a client connection in Server-b is interested in updates fromthe  client connected to Server-a
