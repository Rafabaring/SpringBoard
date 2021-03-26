package red.mug

object KafkaProducerConsumerSbt {
  def main(args: Array[String]): Unit = {

// publishing data to topic
    println("---- Starting Kafka ----")
    KafkaProducer.writeToKafka("second_topic", "sending pulse to publish")
    println("Complete writing to producer in Kafka")

// reading data from topic
    val log_consumer_data = KafkaConsumer.KafkaConsumer("second_topic")
    println("\nComplete reading from consumer in Kafka")

// storing data after reading from topic
    loadStorage.loadS3Storage(log_consumer_data)
    println("complete storage")
  }
}