#!/usr/bin/env python

from kafka import KafkaProducer
import time;

producer = KafkaProducer(bootstrap_servers='192.168.55.253:9092')

while True:
    ts = time.time()
    producer.send('Input', value=str(ts))
    time.sleep(1)