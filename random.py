#! /usr/bin/env python3

import sys

import entropy
import hashlib

def hash(x):
    return hashlib.sha256(hashlib.sha256(x).digest).digest()

# TODO: Crediting and debiting from the entropy pool should be
#       thread safe. 
class EntropyPoolBase:
    def __init__(self, size, min_entropy):
        # TODO: Initialize entropy pool from state of last pool
        #       by saving pool to disk on destruction
        print("Initializing entropy pool")
        self.pool = bytearray(size)
        self.entropy_estimate = 0
        
    def mix_pool_bytes(self, bytes):
        raise NotImplementedException()

    def increase_estimate(self, n_bits):
        raise NotImplementedException()

    def decrease_estimate(self, n_bits):
        raise NotImplementedException()

    def debit_randomness(self, n_bytes):
        if (self.entropy <= min_entropy):
            decrease_estimate(self, n_bytes * 8)
            hashed = hash(self.pool)
            self.mix_pool_bytes(hashed)
            return hashed
        else:
            return None
            
    def credit_randomness(value):
        self.pool = mix_pool_bytes(value, bytes)
        increase_estimate(self, len(value) * 8)
        
if __name__ == '__main__':

    if len(sys.argv) == 1:
        print(psutil.cpu_times())
    elif (sys.argv[1] == "test"):
        
        print("*********************")
        print("    Testing stats")
        print("*********************")
        
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

        print("\n*********************")
        print("Testing entropy pool")
        print("*********************")

        print("Entropy pool {}".format(EntropyPoolBase(256 // 8, 256)))
    else:
        print("Unexpected input")        
