Preparation
1. create docker Postgres
	a. type --> docker pull postgres
	b. type --> docker run --name postgresql -e POSTGRES_USER=myusername -e POSTGRES_PASSWORD=mypassword -p 5432:5432 -d postgres
2. Create docker Hadoop
	link tutorial hadoop
https://towardsdatascience.com/hdfs-simple-docker-installation-guide-for-data-science-workflow-b3ca764fc94b

Python
1. Ingest TR_Products.csv and TR_UserInfo.csv to PostgreSQL

Python mrjob
1. Filter TR_Products.csv that have price more than 10 --> Store result to HDFS --> Also store result to Postgres
2. Aggregate TR_OrderDetails.csv transaction quantity based on date  --> Store result to HDFS --> Also store result to Postgres
3. Aggregate TR_OrderDetails.csv transaction quantity based on date and product  --> Store result to HDFS --> Also store result to Postgres