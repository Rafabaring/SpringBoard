package red.mug

import java.util
import java.util.Properties
import org.apache.kafka.clients.consumer.KafkaConsumer
import scala.collection.JavaConverters._

object KafkaConsumer{

  def KafkaConsumer(topic: String):String = {
    val props = new Properties()
    props.put("bootstrap.servers", "XX.XXX.XXX.X:XXXX") // insert here the IP of the EC2 instance
    props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer")
    props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer")
    props.put("auto.offset.reset", "latest")
    props.put("group.id", "1") // GROUP ID
    val consumer: KafkaConsumer[String, String] = new KafkaConsumer[String, String](props)
    consumer.subscribe(util.Arrays.asList(topic))
    var data_counter = 3

    // log_consumer_data is the string used to log the data in a txt to send to S3
    var log_consumer_data = ""
    while (data_counter != 0) {
      val record = consumer.poll(3000).asScala
      for (data <- record.iterator) {
        data_counter -= 1
        println("data_read", data_counter)
        println(data.value())
        log_consumer_data = log_consumer_data + data.value() + "\n"
        }
      }
    // Returning the string to be logged
    // It will have as many rows as "data_counter"
    log_consumer_data
    }
}
