package red.mug

import java.io.{BufferedWriter, File, FileWriter}
import java.time.LocalDateTime

import com.amazonaws.auth.BasicAWSCredentials
import com.amazonaws.auth.AWSStaticCredentialsProvider
import com.amazonaws.services.s3.AmazonS3ClientBuilder

object loadStorage {

  def check_log(log_to_store: String): Array[String] = {
    val log_list = log_to_store.split(" ")
    log_list
  }

  def loadS3Storage(log_to_store: String): Unit = {
    val AWS_ACCESS_KEY = "XXX"
    val AWS_SECRET_KEY = "YYY"

    val AWSCredentials = new BasicAWSCredentials(AWS_ACCESS_KEY, AWS_SECRET_KEY)
//    val amazonS3Client = new AmazonS3Client(AWSCredentials)
    val s3Client = AmazonS3ClientBuilder
      .standard.withCredentials(new AWSStaticCredentialsProvider(AWSCredentials))
      .withRegion("us-west-2")
      .build

    val bucketName = "//red-mug/kafka_log"          // specifying bucket name
    val fileToUpload = new File("kafka_log")
    val bw = new BufferedWriter(new FileWriter(fileToUpload))

    bw.write(LocalDateTime.now() + " : " + log_to_store.toString())
    bw.close()

    // This will create a bucket for storage
    s3Client.putObject(bucketName, "kafka_log.txt", fileToUpload)
  }

}
