import psutil

# Returns the system-wide number of reads
def read_count():
    count = psutil.disk_io_counters().read_count
    return count

# Returns the system-wide number of writes
def write_count():
    count = psutil.disk_io_counters().write_count
    return count

# Returns system wide number of bytes sent
def bytes_sent():
    sent = psutil.net_io_counters().bytes_sent
    return sent

# Returns system wide number of bytes received
def bytes_recv():
    recv = psutil.net_io_counters().bytes_recv
    return recv

# Returns number of interrupts since boot
def interrupts_count():
    count = psutil.cpu_stats().interrupts
    return count

# Returns the number of context switches since boot
def ctx_switches():
    count = psutil.cpu_stats().ctx_switches
    return count
