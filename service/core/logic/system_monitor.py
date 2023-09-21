import psutil

# Function to monitor RAM usage
def monitor_memory_usage():
    virtual_memory = psutil.virtual_memory()
    total_memory = virtual_memory.total / (1024 ** 3)  # Total RAM in GB
    available_memory = virtual_memory.available / (1024 ** 3)  # Available RAM in GB
    used_memory = virtual_memory.used / (1024 ** 3)  # Used RAM in GB
    memory_percent = virtual_memory.percent  # RAM usage percentage

    print(f"Total Memory: {total_memory:.2f} GB")
    print(f"Available Memory: {available_memory:.2f} GB")
    print(f"Used Memory: {used_memory:.2f} GB")
    print(f"Memory Usage Percentage: {memory_percent:.2f}%")


