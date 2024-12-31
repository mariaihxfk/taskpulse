import psutil
import time

def print_cpu_info():
    print("CPU Usage: ", psutil.cpu_percent())

def print_memory_info():
    memory_info = psutil.virtual_memory()
    print('Memory Usage:', memory_info.percent)

def print_disk_info():
    disk_info = psutil.disk_usage('/')
    print('Disk Usage:', disk_info.percent)

while True:
    print_cpu_info()
    print_memory_info()
    print_disk_info()
    time.sleep(1)