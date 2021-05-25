package red.mug

object KafkaProducerConsumerSbt {
  def main(args: Array[String]): Unit = {

// Establishing a Postgres Connection
    val conn = DBManager.connectPostgres()

// publishing data to topic
    println("---- Starting Kafka ----")
    KafkaProducer.writeToKafka("second_topic", "7")
    println("\nComplete writing to producer in Kafka")

// reading data from topic
    val log_consumer_data = KafkaConsumer.KafkaConsumer("second_topic", conn)
    println("\nComplete reading from consumer in Kafka")

// closing Postregres connection
    DBManager.closeConnectionPostgres(conn)

// storing data after reading from topic
    loadStorage.loadS3Storage(log_consumer_data)
    println("\nComplete storage in S3 bucket")
  }
}