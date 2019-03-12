##09277 박한주


sqoop import \
--table accounts \
--connect jdbc:mysql://localhost/loudacre \
--username training --password training \
--columns "acct_num,first_name,last_name" \
--target-dir /loudacre/accounts/user_info \
--as-textfile


## 1 code result

19/03/10 22:29:55 INFO sqoop.Sqoop: Running Sqoop version: 1.4.6-cdh5.7.0
19/03/10 22:29:55 WARN tool.BaseSqoopTool: Setting your password on the command-line is insecure. Consider using -P instead.
19/03/10 22:29:55 INFO manager.MySQLManager: Preparing to use a MySQL streaming resultset.
19/03/10 22:29:55 INFO tool.CodeGenTool: Beginning code generation
19/03/10 22:29:56 INFO manager.SqlManager: Executing SQL statement: SELECT t.* FROM `accounts` AS t LIMIT 1
19/03/10 22:29:56 INFO manager.SqlManager: Executing SQL statement: SELECT t.* FROM `accounts` AS t LIMIT 1
19/03/10 22:29:56 INFO orm.CompilationManager: HADOOP_MAPRED_HOME is /usr/lib/hadoop-mapreduce
Note: /tmp/sqoop-training/compile/3a261093c02d429d212ad28e98b06709/accounts.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
19/03/10 22:29:58 INFO orm.CompilationManager: Writing jar file: /tmp/sqoop-training/compile/3a261093c02d429d212ad28e98b06709/accounts.jar
19/03/10 22:29:59 WARN manager.MySQLManager: It looks like you are importing from mysql.
19/03/10 22:29:59 WARN manager.MySQLManager: This transfer can be faster! Use the --direct
19/03/10 22:29:59 WARN manager.MySQLManager: option to exercise a MySQL-specific fast path.
19/03/10 22:29:59 INFO manager.MySQLManager: Setting zero DATETIME behavior to convertToNull (mysql)
19/03/10 22:29:59 INFO mapreduce.ImportJobBase: Beginning import of accounts
19/03/10 22:29:59 INFO Configuration.deprecation: mapred.job.tracker is deprecated. Instead, use mapreduce.jobtracker.address
19/03/10 22:29:59 INFO Configuration.deprecation: mapred.jar is deprecated. Instead, use mapreduce.job.jar
19/03/10 22:30:00 INFO Configuration.deprecation: mapred.map.tasks is deprecated. Instead, use mapreduce.job.maps
19/03/10 22:30:00 INFO client.RMProxy: Connecting to ResourceManager at /0.0.0.0:8032
19/03/10 22:30:02 INFO db.DBInputFormat: Using read commited transaction isolation
19/03/10 22:30:02 INFO db.DataDrivenDBInputFormat: BoundingValsQuery: SELECT MIN(`acct_num`), MAX(`acct_num`) FROM `accounts`
19/03/10 22:30:02 INFO db.IntegerSplitter: Split size: 32440; Num splits: 4 from: 1 to: 129761
19/03/10 22:30:02 INFO mapreduce.JobSubmitter: number of splits:4
19/03/10 22:30:02 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1552277434102_0005
19/03/10 22:30:03 INFO impl.YarnClientImpl: Submitted application application_1552277434102_0005
19/03/10 22:30:03 INFO mapreduce.Job: The url to track the job: http://localhost:8088/proxy/application_1552277434102_0005/
19/03/10 22:30:03 INFO mapreduce.Job: Running job: job_1552277434102_0005
19/03/10 22:30:11 INFO mapreduce.Job: Job job_1552277434102_0005 running in uber mode : false
19/03/10 22:30:11 INFO mapreduce.Job:  map 0% reduce 0%
19/03/10 22:30:18 INFO mapreduce.Job:  map 25% reduce 0%
19/03/10 22:30:25 INFO mapreduce.Job:  map 50% reduce 0%
19/03/10 22:30:30 INFO mapreduce.Job:  map 75% reduce 0%
19/03/10 22:30:35 INFO mapreduce.Job:  map 100% reduce 0%
19/03/10 22:30:36 INFO mapreduce.Job: Job job_1552277434102_0005 completed successfully
19/03/10 22:30:37 INFO mapreduce.Job: Counters: 30
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=560468
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=470
		HDFS: Number of bytes written=2615920
		HDFS: Number of read operations=16
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=8
	Job Counters 
		Launched map tasks=4
		Other local map tasks=4
		Total time spent by all maps in occupied slots (ms)=0
		Total time spent by all reduces in occupied slots (ms)=0
		Total time spent by all map tasks (ms)=17678
		Total vcore-seconds taken by all map tasks=17678
		Total megabyte-seconds taken by all map tasks=4525568
	Map-Reduce Framework
		Map input records=129761
		Map output records=129761
		Input split bytes=470
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=247
		CPU time spent (ms)=4030
		Physical memory (bytes) snapshot=494297088
		Virtual memory (bytes) snapshot=8260124672
		Total committed heap usage (bytes)=251920384
	File Input Format Counters 
		Bytes Read=0
	File Output Format Counters 
		Bytes Written=2615920
19/03/10 22:30:37 INFO mapreduce.ImportJobBase: Transferred 2.4947 MB in 36.9565 seconds (69.1248 KB/sec)
19/03/10 22:30:37 INFO mapreduce.ImportJobBase: Retrieved 129761 records.




2.
sqoop import \
--table accounts \
--connect jdbc:mysql://localhost/loudacre \
--username training --password training \
--compression-codec \
org.apache.hadoop.io.compress.SnappyCodec \
--target-dir /loudacre/accounts/user_compressed \
--as-parquetfile


##2 result.


19/03/10 22:33:18 INFO sqoop.Sqoop: Running Sqoop version: 1.4.6-cdh5.7.0
19/03/10 22:33:18 WARN tool.BaseSqoopTool: Setting your password on the command-line is insecure. Consider using -P instead.
19/03/10 22:33:18 INFO manager.MySQLManager: Preparing to use a MySQL streaming resultset.
19/03/10 22:33:18 INFO tool.CodeGenTool: Beginning code generation
19/03/10 22:33:18 INFO manager.SqlManager: Executing SQL statement: SELECT t.* FROM `accounts` AS t LIMIT 1
19/03/10 22:33:18 INFO manager.SqlManager: Executing SQL statement: SELECT t.* FROM `accounts` AS t LIMIT 1
19/03/10 22:33:18 INFO orm.CompilationManager: HADOOP_MAPRED_HOME is /usr/lib/hadoop-mapreduce
Note: /tmp/sqoop-training/compile/6fc8368df0a1ede8f1404bb9b1d48b70/accounts.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
19/03/10 22:33:21 INFO orm.CompilationManager: Writing jar file: /tmp/sqoop-training/compile/6fc8368df0a1ede8f1404bb9b1d48b70/accounts.jar
19/03/10 22:33:21 WARN manager.MySQLManager: It looks like you are importing from mysql.
19/03/10 22:33:21 WARN manager.MySQLManager: This transfer can be faster! Use the --direct
19/03/10 22:33:21 WARN manager.MySQLManager: option to exercise a MySQL-specific fast path.
19/03/10 22:33:21 INFO manager.MySQLManager: Setting zero DATETIME behavior to convertToNull (mysql)
19/03/10 22:33:21 INFO mapreduce.ImportJobBase: Beginning import of accounts
19/03/10 22:33:21 INFO Configuration.deprecation: mapred.job.tracker is deprecated. Instead, use mapreduce.jobtracker.address
19/03/10 22:33:22 INFO Configuration.deprecation: mapred.jar is deprecated. Instead, use mapreduce.job.jar
19/03/10 22:33:23 INFO Configuration.deprecation: mapred.map.tasks is deprecated. Instead, use mapreduce.job.maps
19/03/10 22:33:23 INFO client.RMProxy: Connecting to ResourceManager at /0.0.0.0:8032
19/03/10 22:33:25 INFO db.DBInputFormat: Using read commited transaction isolation
19/03/10 22:33:25 INFO db.DataDrivenDBInputFormat: BoundingValsQuery: SELECT MIN(`acct_num`), MAX(`acct_num`) FROM `accounts`
19/03/10 22:33:25 INFO db.IntegerSplitter: Split size: 32440; Num splits: 4 from: 1 to: 129761
19/03/10 22:33:25 INFO mapreduce.JobSubmitter: number of splits:4
19/03/10 22:33:25 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1552277434102_0006
19/03/10 22:33:25 INFO impl.YarnClientImpl: Submitted application application_1552277434102_0006
19/03/10 22:33:26 INFO mapreduce.Job: The url to track the job: http://localhost:8088/proxy/application_1552277434102_0006/
19/03/10 22:33:26 INFO mapreduce.Job: Running job: job_1552277434102_0006
19/03/10 22:33:34 INFO mapreduce.Job: Job job_1552277434102_0006 running in uber mode : false
19/03/10 22:33:34 INFO mapreduce.Job:  map 0% reduce 0%
19/03/10 22:33:42 INFO mapreduce.Job:  map 25% reduce 0%
19/03/10 22:33:49 INFO mapreduce.Job:  map 50% reduce 0%
19/03/10 22:33:55 INFO mapreduce.Job:  map 75% reduce 0%
19/03/10 22:34:01 INFO mapreduce.Job:  map 100% reduce 0%
19/03/10 22:34:01 INFO mapreduce.Job: Job job_1552277434102_0006 completed successfully
19/03/10 22:34:01 INFO mapreduce.Job: Counters: 30
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=560256
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=470
		HDFS: Number of bytes written=8942356
		HDFS: Number of read operations=16
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=8
	Job Counters 
		Launched map tasks=4
		Other local map tasks=4
		Total time spent by all maps in occupied slots (ms)=0
		Total time spent by all reduces in occupied slots (ms)=0
		Total time spent by all map tasks (ms)=21209
		Total vcore-seconds taken by all map tasks=21209
		Total megabyte-seconds taken by all map tasks=5429504
	Map-Reduce Framework
		Map input records=129761
		Map output records=129761
		Input split bytes=470
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=305
		CPU time spent (ms)=6990
		Physical memory (bytes) snapshot=545615872
		Virtual memory (bytes) snapshot=8283398144
		Total committed heap usage (bytes)=251920384
	File Input Format Counters 
		Bytes Read=0
	File Output Format Counters 
		Bytes Written=8942356
19/03/10 22:34:01 INFO mapreduce.ImportJobBase: Transferred 8.5281 MB in 38.8229 seconds (224.9386 KB/sec)
19/03/10 22:34:01 INFO mapreduce.ImportJobBase: Retrieved 129761 records.





3.sqoop import \
--table accounts \
--connect jdbc:mysql://localhost/loudacre \
--username training --password training \
--table accounts \
--where "state='CA'" \
--target-dir /loudacre/accounts/CA \
-z \
--as-parquetfile

##3.result

19/03/10 22:35:00 INFO sqoop.Sqoop: Running Sqoop version: 1.4.6-cdh5.7.0
19/03/10 22:35:00 WARN tool.BaseSqoopTool: Setting your password on the command-line is insecure. Consider using -P instead.
19/03/10 22:35:01 INFO manager.MySQLManager: Preparing to use a MySQL streaming resultset.
19/03/10 22:35:01 INFO tool.CodeGenTool: Beginning code generation
19/03/10 22:35:01 INFO tool.CodeGenTool: Will generate java class as codegen_accounts
19/03/10 22:35:01 INFO manager.SqlManager: Executing SQL statement: SELECT t.* FROM `accounts` AS t LIMIT 1
19/03/10 22:35:01 INFO manager.SqlManager: Executing SQL statement: SELECT t.* FROM `accounts` AS t LIMIT 1
19/03/10 22:35:01 INFO orm.CompilationManager: HADOOP_MAPRED_HOME is /usr/lib/hadoop-mapreduce
Note: /tmp/sqoop-training/compile/a6216d920982637ed18676f81ee48073/codegen_accounts.java uses or overrides a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
19/03/10 22:35:04 INFO orm.CompilationManager: Writing jar file: /tmp/sqoop-training/compile/a6216d920982637ed18676f81ee48073/codegen_accounts.jar
19/03/10 22:35:04 WARN manager.MySQLManager: It looks like you are importing from mysql.
19/03/10 22:35:04 WARN manager.MySQLManager: This transfer can be faster! Use the --direct
19/03/10 22:35:04 WARN manager.MySQLManager: option to exercise a MySQL-specific fast path.
19/03/10 22:35:04 INFO manager.MySQLManager: Setting zero DATETIME behavior to convertToNull (mysql)
19/03/10 22:35:04 INFO mapreduce.ImportJobBase: Beginning import of accounts
19/03/10 22:35:04 INFO Configuration.deprecation: mapred.job.tracker is deprecated. Instead, use mapreduce.jobtracker.address
19/03/10 22:35:05 INFO Configuration.deprecation: mapred.jar is deprecated. Instead, use mapreduce.job.jar
19/03/10 22:35:06 INFO manager.SqlManager: Executing SQL statement: SELECT t.* FROM `accounts` AS t LIMIT 1
19/03/10 22:35:06 INFO manager.SqlManager: Executing SQL statement: SELECT t.* FROM `accounts` AS t LIMIT 1
19/03/10 22:35:07 INFO Configuration.deprecation: mapred.map.tasks is deprecated. Instead, use mapreduce.job.maps
19/03/10 22:35:07 INFO client.RMProxy: Connecting to ResourceManager at /0.0.0.0:8032
19/03/10 22:35:09 INFO db.DBInputFormat: Using read commited transaction isolation
19/03/10 22:35:09 INFO db.DataDrivenDBInputFormat: BoundingValsQuery: SELECT MIN(`acct_num`), MAX(`acct_num`) FROM `accounts`
19/03/10 22:35:09 INFO db.IntegerSplitter: Split size: 32440; Num splits: 4 from: 1 to: 129761
19/03/10 22:35:09 INFO mapreduce.JobSubmitter: number of splits:4
19/03/10 22:35:10 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1552277434102_0007
19/03/10 22:35:10 INFO impl.YarnClientImpl: Submitted application application_1552277434102_0007
19/03/10 22:35:10 INFO mapreduce.Job: The url to track the job: http://localhost:8088/proxy/application_1552277434102_0007/
19/03/10 22:35:10 INFO mapreduce.Job: Running job: job_1552277434102_0007
19/03/10 22:35:19 INFO mapreduce.Job: Job job_1552277434102_0007 running in uber mode : false
19/03/10 22:35:19 INFO mapreduce.Job:  map 0% reduce 0%
19/03/10 22:35:30 INFO mapreduce.Job:  map 25% reduce 0%
19/03/10 22:35:39 INFO mapreduce.Job:  map 50% reduce 0%
19/03/10 22:35:49 INFO mapreduce.Job:  map 75% reduce 0%
19/03/10 22:35:59 INFO mapreduce.Job:  map 100% reduce 0%
19/03/10 22:35:59 INFO mapreduce.Job: Job job_1552277434102_0007 completed successfully
19/03/10 22:35:59 INFO mapreduce.Job: Counters: 30
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=569024
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=65306
		HDFS: Number of bytes written=5904589
		HDFS: Number of read operations=272
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=40
	Job Counters 
		Launched map tasks=4
		Other local map tasks=4
		Total time spent by all maps in occupied slots (ms)=0
		Total time spent by all reduces in occupied slots (ms)=0
		Total time spent by all map tasks (ms)=33450
		Total vcore-seconds taken by all map tasks=33450
		Total megabyte-seconds taken by all map tasks=8563200
	Map-Reduce Framework
		Map input records=129761
		Map output records=129761
		Input split bytes=470
		Spilled Records=0
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=1112
		CPU time spent (ms)=16140
		Physical memory (bytes) snapshot=775614464
		Virtual memory (bytes) snapshot=8296341504
		Total committed heap usage (bytes)=251920384
	File Input Format Counters 
		Bytes Read=0
	File Output Format Counters 
		Bytes Written=0
19/03/10 22:35:59 INFO mapreduce.ImportJobBase: Transferred 5.6311 MB in 51.9258 seconds (111.0469 KB/sec)
19/03/10 22:35:59 INFO mapreduce.ImportJobBase: Retrieved 129761 records.