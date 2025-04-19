# High-level Design
### 1) Users should be able to upload a file from any device
   - Get preSignedURL from S3, users can directly upload to S3
### 2)  Users should be able to download a file
   - Get the presigned URL from S3 to download
   - Use CDN for low latency and cached files
### 3) Users can share the file with others
  - Having a shareList[] for each file is slow for querying
  - Have a separate sharedTable DB that gets updated when shared for a userId
### 4) Sync across devices
  - Local to Remote: monitor file change and upload the file with preSignedURL
  - Remote to Local:
    - Either Client polls
    - Websockets or SSE from File Service to Client
    - Use hybrid method: for fresh file, use websocket, for least used file: use polling
   
# Deep Dives
### 1) How can you support large files?
  - limitation on api gateway, timeouts
  - Client splits the files into chunks
  - Each chunk has a chunk ID
  - User chunks and uploads to S3, S3 event notifications to update metadata and chunkId as 'uploaded'
  - Chunk has a file fingerprint, and it is used as key
### 2) How can we make uploads, downloads, and syncing as fast as possible?
  - Chunk the file based on bandwidth
  - Use CDN for fast file access
  - Use file compression at client & server
  - Check for the chunk ID, which is modified
### 3) How can you ensure file security?
  - Presigned URL only for a short time
  - Encrypt the file in S3
