import subprocess

groups_file = "groups.txt"
kafka_port = "9092"
ip_address = subprocess.check_output(['hostname', '-I']).decode().split()[0]

with open(groups_file) as f:
    group = f.readline().strip()

command = f'/opt/Apache/kafka/bin/kafka-consumer-groups --bootstrap-server {ip_address}:{kafka_port} --describe --group {group}'
result = subprocess.check_output(command, shell=True).decode()
print(result)
