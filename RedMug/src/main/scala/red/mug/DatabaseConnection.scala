package red.mug

import java.sql.{Connection, DriverManager, ResultSet}
import java.time.LocalDateTime

object DBManager {
  def connectPostgres(): Connection = {
    classOf[org.postgresql.Driver]
    val con_st = "jdbc:postgresql://db_host/your_db?user=db_user"
    val conn = DriverManager.getConnection(con_st)
    conn
  }

  def database_input(message: Int): String = {
    message.toString
  }

  def insertIntoPostgres(conn: Connection, input_value: String): Unit = {
      val stm = conn.createStatement(ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY)
      stm.execute("INSERT INTO sensor_input VALUES ('" + LocalDateTime.now() +"', " + input_value + ")")
  }

  def closeConnectionPostgres(conn: Connection): Unit= {
    conn.close()
  }
}