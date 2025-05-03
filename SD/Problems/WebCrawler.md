# WEB CRAWLER

## Functional Req
- Crawl the web starting from a given set of seed URLS.
- Extract text data from each web page and store the text for later processing.

## Non-Functional Req
- Fault tolerance to handle failures gracefully and resume crawling without losing progress.
- Politeness in adhering to robots.txt and not overloading website servers inappropriately.
- Efficiency to crawl the web in under 5 days.
- Scalability to handle 10B pages.

## System Interface
 - Input: seed URLS
 - Output: text data extracted from web pages

## Data Flow
- Take seed URLS and add to the queue
- req IP from DNS
- get HTML page from IP
- Extract data and URL from HTML and put URL in queue
- Store data in the DB
- repeat

## High-Level Design
- Simple system with queue, crawl service and DB

## Deep Dives
### 1) How can we ensure we are fault-tolerant and don't lose progress?
- Split the system into small pipelined stages
- Have a MetaData DB to store the info on URL status(Postgresql/Mysql), upon failure, get the status of the URL
- The processing queue stores the ID of the URL, and storing the HTML files in the queue is expensive
- What about if we fail to fetch a URL?
  - URL fetch is likely to fail
  - Use Kafka queue - doesn't inherently support retries, store failed URLS and do retries with exponential backoff
  - Use Amazon SQS with exponential backoff - can configure retries, has visibility timeout. Cap the maximum retries.
- What happens if a crawler goes down?
  - Have a backup crawler to take up where the first crawler left off
  - Kafka: crawler tracks progress with offsets
  - SQS: has a visibility timeout for the crawler to fetch
  
### 2) How can we ensure politeness and adhere to robots.txt?
- Robots.txt has "User agent", "Disallow", "crawl delay".
- To ensure politeness, adhere to robots.txt and ratelimiting
- robots.txt
  - is a one-time download(may vary), don't scan the disallow directories, and poll for the specified crawl delay
  - During dequeue from the queue, if the URL is within the crawl-delay, push it back to the queue
  - Store the file in the metadata DB
- rate-limiting
  - Have a Redis cache and store the last polled time in it. use sliding-window algo
  - Check the cache before polling the website

### 3) How to scale to 10B pages and efficiently crawl them in under 5 days?
- 10B pages in 5 days,
- AWS instance 400 Gbps / 8 bits/byte / 2MB/page = 25,000 pages/second, we use 30% of it: 25,000 pages/second * 30% = 7,500 pages/second.
- 10^10/7,500 pages/second ~ 15 days, divide to 4 machines = 3.5 days/machine
- Parser workers: Scale according to the crawlers
- DNS: have multiple DNS providers or cache the response from DNS
- Efficiency: What if multiple link points to the same page?
  - Hash and store the index in the Metadata DB
  - Bloom filters: more efficient but less accurate
- Traps: Have a max depth to crawl till that depth
