### **Apache Spark - Short Summary**  

#### **1. What is Spark?**  
- A **fast, distributed** big data processing engine for large-scale analytics.  
- Optimized for **in-memory computation** (100x faster than Hadoop MapReduce).  

#### **2. Key Features**  
- **Speed**: Uses RAM to cache data (avoids disk I/O bottlenecks).  
- **Ease of Use**: APIs in **Python (PySpark), Scala, Java, R, SQL**.  
- **Unified Engine**: Supports batch, streaming, machine learning, and graph processing.  
- **Fault Tolerance**: Recovers lost data automatically.  

#### **3. Core Components**  
- **Spark Core**: Base engine (task scheduling, memory management).  
- **Spark SQL**: Structured data processing (DataFrames, SQL queries).  
- **Spark Streaming**: Real-time data processing (micro-batches).  
- **MLlib**: Machine learning library (algorithms, pipelines).  
- **GraphX**: Graph processing (e.g., social networks).  

#### **4. How It Works**  
- **Resilient Distributed Datasets (RDDs)**: Immutable data partitions (fault-tolerant).  
- **DataFrames/Datasets**: Higher-level APIs for structured data.  
- **Lazy Evaluation**: Optimizes workflows before execution.  

#### **5. Use Cases**  
- **ETL pipelines** (process large datasets).  
- **Real-time analytics** (e.g., fraud detection).  
- **Machine learning** (training models on big data).  

#### **6. Spark vs. Hadoop**  
| Feature       | Spark                          | Hadoop MapReduce               |  
|--------------|-------------------------------|--------------------------------|  
| **Speed**    | In-memory (fast)              | Disk-based (slower)            |  
| **Ease**     | Simple APIs (Python/SQL)      | Complex Java code              |  
| **Use Cases**| Batch + streaming + ML        | Batch-only                     |  

#### **7. Deployment**  
- **Standalone**: Single machine.  
- **Cluster**: **YARN** (Hadoop), **Mesos**, or **Kubernetes**.  
- **Cloud**: AWS EMR, Databricks, GCP Dataproc.  

---

**When to Use Spark?** → For large-scale, fast data processing (ETL, analytics, ML).  
