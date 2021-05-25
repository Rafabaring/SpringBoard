name := "RedMug"

version := "0.1"

scalaVersion := "2.11.8"

libraryDependencies ++= Seq(
  "org.apache.spark"  %% "spark-core" % "2.4.5" % "provided", // provided meaning it will be installed in the EMR
  "org.apache.spark"  %% "spark-sql" % "2.4.5" % "provided",
  "com.databricks"    % "spark-redshift_2.10" % "3.0.0-preview1", // used on S3 storage
  "jp.co.bizreach"    %% "aws-s3-scala" % "0.0.15",
  "org.apache.hadoop" % "hadoop-aws" % "2.7.3",
  "org.scalatest" %% "scalatest" % "3.2.9" % "test",
  "com.amazonaws"     % "aws-java-sdk" % "1.11.950",
  "org.apache.kafka"  %% "kafka" % "2.1.0",
  "org.postgresql" % "postgresql" % "9.3-1102-jdbc41"
)
