
# Prerequisites 

 - Virtualbox 
 - Ansible

# Shortcuts
- Prometheus: http://192.168.55.252:9090
- Grafana: http://192.168.55.252:3000 (admin/admin)

  
# To initialize nodes:

    vagrant up



# Prometheus features: 
Kafka metrics or general metrics can be seen from http://192.168.55.252:9090/graph

    insert expression, e.g. kafka_log_log_size

 
## Worker 
After initializing the worker node, both py (producer & consumer/producer) will start automatically.

    systemctl status producer 
    systemctl status consumer

 
Service is logging current progress to file **/var/log/consumer.log**  
May be seen by executing command on "**Kafka**" node:

    tail -f /var/log/kafka-input.log
    tail -f /var/log/kafka-output.log

  
# Monitoring  
Monitoring solution used for this project is **Prometheus**. (node exporter, jmx exporter, kafka exporter).  
**Grafana** is used for showing dasboards (3 total).

# Points of discussion
 -  RPM packages
-  Efficiency
-  General cleanliness
