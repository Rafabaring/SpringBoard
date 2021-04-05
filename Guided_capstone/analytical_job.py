from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# Creating a view for the EOD data
trades_and_quotes_last_df.createOrReplaceTempView("trades_and_quotes_last_df")


# Latest trade price before the quote
latest_trade_price = spark.sql('''
SELECT
	tr.trade_dt,
	MIN(tr.trade_pr) min_trade_pr
FROM
	trades_and_quotes_last_df tr
LEFT JOIN
	(SELECT *
	 FROM
	 	trades_and_quotes_last_df
	 WHERE
	 	rec_type = 'Q'
	) qt
ON
	tr.symbol = qt.symbol
	AND tr.exchange = qt.exchange
WHERE
	tr.rec_type = 'T'
	AND tr.event_tm > qt.event_tm
GROUP BY
	tr.trade_dt
''')

# Creating a view for moving average
latest_trade_price.write.saveAsTable("latest_trade_price_tbl")



# Getting the moving average
moving_average = spark.sql('''
SELECT
	symbol,
	exchange,
	event_tm,
	event_seq_nb,
	bid_pr,
	AVG(bid_pr) OVER(PARTITION BY symbol ORDER BY event_tm
					   ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS moving_average
FROM
	trades_and_quotes_last_df
WHERE
	rec_type = 'Q'
''')


# Creating a view for moving average
moving_average.write.saveAsTable("moving_average_tbl")
