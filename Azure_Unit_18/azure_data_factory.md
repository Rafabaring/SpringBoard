
# Azure Data Factory insights and thoughts:


### 1. Why should one use Azure Key Vault when working in the Azure environment? What are the pros and cons? What are the alternatives?

Azure Key Vault is a Microsoft solution created to store keys and identifiers facilitating the authentification of other users and applications. In my personal experience, authentication is always a pain point managed by env files depending on the environment you are developing. When working with KeyVault, the enablement of different services is much easier. One example is the connection with DataBases. In the past, I had to deal with many files holding credentials. And that’s odd because each developer can have it in their way. When setting up KeyVault, the database can read from it to access the necessary credentials.

I would recommend the KeyVault to expand the ability to offer secure services. If other applications or services are also in the Azure environment, it just facilitates communications between services.

As an alternative, and also pointing out the cons, I would refer to the familiarity of other developers. At least in my experience, the alternative, and also what most developers are familiar with it are the traditional methods to store credentials (as I mentioned above, setting up env files and ENV variables). I would point out as a con the necessity of other developers to learn how to implement this solution. Although, the learning curve to get up and running with Key Vault is not steep at all. So definitely recommended.

### 2. How do you achieve loop functionality within an Azure Data Factory pipeline? Why would you need to use this functionality in a data pipeline?

Data Factory allows moving data from one service to the other. It manages multiple Integration Runtime jobs which, by itself, manages as many tasks as you define. Let’s say you are managing a social media app. One of the services generates and drops JSON files in Blob storage. The goal is to move daily created JSON files into a SQL database for analytics to query and come up with insights. The Data Factory will manage the Integration Runtime responsible for each step to pull and load the JSON file into the SQL database.

This functionality is important because we are generating data every day, and we want to keep it up to date. “Looping” the pipeline means having the most recent information, which ultimately means business advantage.

If you want to run the looping once, as an ad-hoc project, let’s say if you are running a migration from one database to another, you can easily use any looping method to run the same job as much as you want. But if you are looking to keep a database up to date in a timely fashion, you should probably use a job orchestration/scheduler

### 3. What are expressions in Azure Data Factory? How are they helpful when designing a data pipeline? Please explain with an example.

Expressions are used to modify variables in the pipeline such as naming, path, and other parameters. Also to add logic in case of evaluation a statement in a pipeline.
One way I see this being extremely important is in case you want to keep some timely control over the tasks being performed.

Let’s say the pipeline generates a file every day and stores it in a bucket. It is important to distinguish the file name from the date it was generated. Otherwise, all files would have the same name and the bucket would be very confusing.

In this example, I can use expressions to automatically add the timestamp at the end of each file_name.

To do this in Azure, I would add this piece of code to the “add dynamic content” box:
```
@concat (
“name_of_the_file’,
utcnow(),
‘.json’
)
```

### 4. What are the pros and cons of parametrizing a dataset’s activity in Azure Data Factory?
Parametrizing is the ability to “create variables” in the pipeline. Especially important when we start to scale up the pipeline operation and we might be interested in re-utilizing the pipeline for other inputs (and create different outputs)

This is better explained with an example:
Imagine we create a simple pipeline that takes as input a CSV file runs a python job aggregating the data by day and storing it in a database. If we hardcode the input as car_sales_log.csv, it will store daily car sales. But let’s say we want to use the same pipeline with the boat_sales_log.csv, so we can have daily boat sales. In this case, we can parametrize the input variable CSV file for replication of the pipeline. So this is one of the pros in parametrizing the pipeline, it enables and facilitates reproducibility of the pipeline.
On the other hand, we can parametrize parts of the pipeline that is not necessary, meaning, it will hardly be modified, over-complicating the pipeline. In my personal experience, pipelines on this matter tend to be harder to understand

So, in broad terms, I would say that parametrizing is great for scalability and reproducibility of the pipeline operations but, if it’s overly used, can create a hard to comprehend pipeline

### 5. What are the different supported file formats and compression codecs in Azure Data Factory? When will you use a Parquet file over an ORC file? Why would you choose an AVRO file format over a Parquet file format?

According to this Microsoft article, these are the files and codecs supported by Azure DF:
https://docs.microsoft.com/en-us/azure/data-factory/supported-file-formats-and-compression-codecs
* **Avro format**
* **Binary format**
* **Delimited text format**
* **Excel format**
* **JSON format**
* **ORC format**
* **Parquet format**
* **XML format**


Parquet, ORC, and AVRO are different types of files formatted, as usual, choosing which file to use will always depend on the requisites of the project.
But in overall, I evaluate these three formats in three separate variables:
* **Human readable**
* **Storage / size / compression**
* **What it will be used for**

Let’s say we are talking about a company with a relatively small dataset, a small engineering team to maintain and develop the data platform, and a few excited analysts, I would suggest using ORC type of data where it could easily work on a relational database, with many references on the internet, easier to maintain, and relatively familiar table-oriented view. But if we are aiming for another type of data usage, to serve as input for machine learning model in production, where latency has to be close to none and (almost) never will be used by analytics, I would recommend a faster more robust solution with a non-relational database making use of JSON format
