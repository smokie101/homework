
# Prerequisites 

 - Virtualbox 
 - Ansible

# Shortcuts
- Prometheus: http://192.168.55.252:9090
- Grafana: http://192.168.55.252:3000

  
# To initialize nodes:

    vagrant up



# Prometheus features: 
Kafka metrics or general metrics can be seen from http://192.168.55.252:9090/graph

    insert expression, e.g. kafka_log_log_size

 
## Worker 
After initializing the worker node, both py (producer & consumer/producer) will start automatically.

    systemctl status producer 
    systemctl status consumer

 
Service is logging current progress (when it takes messages from queue) to file **/var/log/consumer.log**  
You can watch it by:

    tail -f /var/log/consumer.log


  
# Monitoring  
Monitoring solution used for this project is **Prometheus**.  
**Grafana** is used for showing dasboards.  
## Host auto-discovery
**node_exporter** (main system metrics) is automatically discovered by prometheus via **consul**.
New hosts will appear in consul hosts list and in grafana system-overview's dropdown list.  
## Stress test  
To test that monitoring solution works correctly "**stress**" package is installed on all server.  
After running following commands soon enough "**alerting rules**" will highlight triggered rule  
here: http://192.168.55.254:9090/alerts  
Basic parameters test:  

CPU:  

    stress -c 2  

Disk operations:  

    stress --io 1

  
RAM: (will take some time to trigger)  

    stress --vm-bytes $(awk '/MemFree/{printf "%d\\n", $2 * 0.9;}' < /proc/meminfo)k --vm-keep -m 1
