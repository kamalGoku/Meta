# KAFKA

### Basic Terminology and Architecture
- made of multiple *brokers*, they are individual servers serving clients
- Each broker has multiple *partitions*
- *topic* is the logical grouping of partitions
- If Kafka is a message queue, the consumer gives an ack
- If Kafka is a streaming service, the consumer doesn't give an ack
  
### How does it work?
- has 3 fields,
  - key: identify the partition
  - timestamp - to order the message in the partition
  - headers - to give metadata on msg
  
### When to use Kafka in your interview
- either message queue or stream
- message queue use case
  - in youtube to precoess video asynchrnously
  - in ticketmaster as virtual waiting queue
  - decouple producer and consumer, poducer rate >>> consumer rate
- stream
  - in Ad CLick aggregator to process clicks
  - in FB live comments to as pub/sub, where many consumers consume a producer

### What you should know about Kafka for System Design Interviews
#### Scalability
- Horizontal scaling with many brokers
- Partitioning
- Hot Partition? by having a compound key or no key

#### Fault Tolerance and Durability
- having offset
- rebalcing with reamining consumers

#### Handling Retries and Errors
- Producer and consumer retries
  
#### Performance Optimizations
- Batch processing settings

#### Retention Policies
- retention time and space
