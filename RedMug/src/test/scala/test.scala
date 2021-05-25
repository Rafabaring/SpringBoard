import collection.mutable.Stack
import org.scalatest._
import flatspec._
import matchers._
import red.mug.{DBManager, KafkaProducer, loadStorage}

class ExampleSpec extends AnyFlatSpec with should.Matchers {

  "A Message" should "converted to a string" in {
    val input_test = KafkaProducer.validate_message(9)
    input_test shouldBe a [String]
  }

  it should "stored as a string" in {
    val db_input = DBManager.database_input(9)
    db_input shouldBe a [String]
  }

  "Log message" should "an array of string" in {
    val log_message = loadStorage.check_log("2 5 1 5 9")
    log_message shouldBe a [Array[_]]
  }
}