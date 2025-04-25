# WEB CRAWLER

## Functional Req
- Crawl the web starting from a given set of seed URLs.
- Extract text data from each web page and store the text for later processing.

## Non-Functional Req
- Fault tolerance to handle failures gracefully and resume crawling without losing progress.
- Politeness to adhere to robots.txt and not overload website servers inappropriately.
- Efficiency to crawl the web in under 5 days.
- Scalability to handle 10B pages.

## High-Level Design
- Simple system with queue, crawl service and DB

## Deep Dives
### 1) How can we ensure we are fault-tolerant and don't lose progress?
- Split the system into small pipelined stages
- Have a MetaData DB to store the info on URL status(Postgresql/Mysql), upon failure get statu on the URL
- 
### 2) How can we ensure politeness and adhere to robots.txt?
### 3) How to scale to 10B pages and efficiently crawl them in under 5 days?
