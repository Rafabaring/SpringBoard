# generator/app.py
import os
import json
from time import sleep
from kafka import KafkaProducer
from transactions import create_random_transaction

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        # Encode all values as JSON
        # value_deserializer=lambda value: json.loads(value)
    )
    while True:
        transaction = create_random_transaction()
        message = json.dumps(transaction)
        producer.send(TRANSACTIONS_TOPIC, value=transacztion)
        print("TESTING")  # DEBUG
        print(transaction)  # DEBUG
        sleep(SLEEP_TIME)