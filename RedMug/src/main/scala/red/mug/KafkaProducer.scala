package red.mug

import java.util.Properties
import org.apache.kafka.clients.producer.{KafkaProducer, ProducerRecord}


object KafkaProducer{

  // Producer method
  def writeToKafka(topic: String, message: String): Unit = {
    val props = new Properties()
    props.put("bootstrap.servers", "XX.XXX.XXX.X:XXXX") // insert here the IP of the EC2 instance
    props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
    props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")
    val producer = new KafkaProducer[String, String](props)
    val record = new ProducerRecord[String, String](topic, "key", message)
    producer.send(record)
    producer.close()
  }
}
