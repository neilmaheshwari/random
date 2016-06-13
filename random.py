#! /usr/bin/env python3

import sys

import entropy

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print(psutil.cpu_times())
    elif (sys.argv[1] == "test"):
        print("CPU user time: {}".format(
            entropy.cpu_user_time()))
        print("CPU utilization: {}".format(
            entropy.cpu_utilization_percentages(0.1)))
        print("Read count: {}".format(entropy.read_count()))
        print("Write count: {}".format(entropy.write_count()))
        print("Bytes sent: {}".format(entropy.bytes_sent()))
        print("Bytes received: {}".format(entropy.bytes_recv()))
        print("Interrupts count: {}".format(entropy.interrupts_count()))
        print("Context switches: {}".format(entropy.ctx_switches()))
    else:
        print("Unexpected input")        
