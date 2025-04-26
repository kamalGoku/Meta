# WEB CRAWLER

## Functional Req
- Crawl the web starting from a given set of seed URLS.
- Extract text data from each web page and store the text for later processing.

## Non-Functional Req
- Fault tolerance to handle failures gracefully and resume crawling without losing progress.
- Politeness in adhering to robots.txt and not overloading website servers inappropriately.
- Efficiency to crawl the web in under 5 days.
- Scalability to handle 10B pages.

## High-Level Design
- Simple system with queue, crawl service and DB

## Deep Dives
### 1) How can we ensure we are fault-tolerant and don't lose progress?
- Split the system into small pipelined stages
- Have a MetaData DB to store the info on URL status(Postgresql/Mysql), upon failure, get the status on the URL
- The processing queue stores the ID of the URL, and storing the HTML files in the queue is expensive
- What about if we fail to fetch a URL?
  - URL fetch is likely to fail
  - Use Kafka queue - doesn't inherently support retries, store failed URLS and do retries with exponential backoff
  - Use Amazon SQS with exponential backoff - can configure retries, has visibility timeout. Cap the maximum retries.
- What happens if a crawler goes down?
  - Have a backup crawler to take up where the first crawler left off
  - Both Kafka and SQS store the events
  
### 2) How can we ensure politeness and adhere to robots.txt?
- Robots.txt has "User agent", "Disallow", "crawl delay".
- To ensure politeness, adhere to robots.txt and ratelimiting
- robots.txt
  - is one-time download(may vary), don't scan the disallow directories, and poll for specified crawl delay
  - during dequeue from queue, if the URL is within crawl-delay, push it back to queue
  - store the file in metadata DB
- rate-limiting
  - have a redis cache and store the last polled time in it. use sliding-window algo
  - check the cache before polling website
- 
### 3) How to scale to 10B pages and efficiently crawl them in under 5 days?
