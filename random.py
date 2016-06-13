#! /usr/bin/env python3

import sys

import psutil

# Returns the seconds the CPU has spent in user mode
# TODO: Use nano or milliseconds
def cpu_user_time():
    time = psutil.cpu_times().user
    return time

# Returns the system-wide CPU utilization as a percentage for each
# CPU. Blocks for i seconds. 
def cpu_utilization_percentages(i):
    percents = psutil.cpu_times_percent(interval = i, percpu = True)
    return percents

# Returns the system-wide number of reads
def read_count():
    count = psutil.disk_io_counters().read_count
    return count

# Returns the system-wide number of writes
def write_count():
    count = psutil.disk_io_counters().write_count
    return count

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print(psutil.cpu_times())
    elif (sys.argv[1] == "test"):
        print("CPU user time: {}".format(cpu_user_time()))
        print("CPU utilization: {}".format(cpu_utilization_percentages(0.1)))
        print("Read count: {}".format(read_count()))
        print("Write count: {}".format(write_count()))
    else:
        print("Unexpected input")        
