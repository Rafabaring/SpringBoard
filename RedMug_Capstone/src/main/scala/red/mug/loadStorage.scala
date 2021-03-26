package red.mug

import java.io.{BufferedWriter, File, FileWriter}





import com.amazonaws.auth.BasicAWSCredentials
import com.amazonaws.auth.AWSStaticCredentialsProvider
import com.amazonaws.services.s3.AmazonS3ClientBuilder

object loadStorage {

  def loadS3Storage(log_to_store: String): Unit = {
    val AWS_ACCESS_KEY = AWS_ACCESS_KEY
    val AWS_SECRET_KEY = AWS_SECRET_KEY

    val AWSCredentials = new BasicAWSCredentials(AWS_ACCESS_KEY, AWS_SECRET_KEY)
//    val amazonS3Client = new AmazonS3Client(AWSCredentials)
    val s3Client = AmazonS3ClientBuilder.standard.withCredentials(new AWSStaticCredentialsProvider(AWSCredentials)).build

    val bucketName = "//red-mug/kafka_log"          // specifying bucket name
    val fileToUpload = new File("kafka_log")
    val bw = new BufferedWriter(new FileWriter(fileToUpload))

    bw.write(log_to_store.toString())
    bw.close()

    // This will create a bucket for storage
    s3Client.putObject(bucketName, "kafka_log.txt", fileToUpload)
  }

}
