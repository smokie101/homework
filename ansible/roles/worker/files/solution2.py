#!/usr/bin/env python

from kafka import KafkaConsumer
from kafka import KafkaProducer
from datetime import datetime

consumer = KafkaConsumer('Input',bootstrap_servers='192.168.55.253:9092')

producer = KafkaProducer(bootstrap_servers='192.168.55.253:9092')

for message in consumer:
    x = float(message.value)
    dt = datetime.utcfromtimestamp(x).isoformat('T') + 'Z'
    producer.send('Output', value=str(dt))