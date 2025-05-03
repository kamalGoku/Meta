## Functional Req
  - Users should be able to view events
  - Users should be able to search for events
  - Users should be able to book tickets to events

## Non-Functional Req
 - Highly available for the search of events
 - Prioritise consistency for booking tickets
 - Scalable to a large number of events(10M events)
 - low latency for viweing events

## Entities
  - User, Event, Booking, Ticket, Venue, Performer
    
## API
  - GET /events/:eventId
  - POST /bookings/:eventId ->bookingId
    {
      ticketId = []
      paymentDetails = ''
    }
  - GET /events/search?keyword={keyword}&start={start_date}&end={end_date}&pageSize={page_size}&page={page_number} -> Event[]

## High-Level Design

### 1) Users should be able to view events
  - Event Service and Event DB
    
### 2) Users should be able to search for events
  - Search service and Event DB

### 3) Users should be able to book tickets to events
  - Booking Service and DB, have a booking table and a Ticket Table
  - Payment processor/service to process payments

## Deep Dives

### 1) How do we improve the booking experience by reserving tickets?
  - Having a lock on DB is bad, gives load to DB, the Postgresql DB has no TTL support
  - Having a cron job to have a TTL and release the lock, but it's not fast enough. Booking will have 'available', 'reserved', and 'booked' states
  - Have a status + expiry time in DB, this will be good, but the query time is increased because of two fields query/
  - Distributed Lock(Redis) to have an entry, the DB will have only 'available' and 'booked'

### 2) How will the view API scale to support 10s of millions of concurrent requests during popular events?
  - Caching popular events
  - Horizontal scaling and Load balancing to many Event Services
 
### 3) How will the system ensure a good user experience during high-demand events with millions simultaneously booking tickets?
  - SSE events from the booking service for seat maps, but not useful for very popular events
  - Great Sol: Virtual waiting queue for queuing the customers for very popular events. Users can view the seat map during deque.
    
### 4) How can you improve search to ensure we meet our low-latency requirements?
  - Querying the DB is slow
  - Having a full-text indexing in the DB and query optimisation.
  - Having an Elastic search for the queries. Have a Change Data Capture(CDC), which captures events in the main DB
    
### 5) How can you speed up frequently repeated search queries and reduce load on our search infrastructure?
  - Query result caching
  - Use CDN for storing the results to serve geoagrically near server
