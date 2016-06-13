#! /usr/bin/env python3

import sys

import entropy
import hashlib
import binascii

pool_size = 256

def hash(x):
    return hashlib.sha256(bytearray(hashlib.sha256(x).digest())).digest()

# TODO: Crediting and debiting from the entropy pool should be
#       thread safe. 
class EntropyPoolBase:
    def __init__(self, min_entropy):
        # TODO: Initialize entropy pool from state of last pool
        #       by saving pool to disk on destruction
        print("Initializing entropy pool")
        self.pool = bytearray(pool_size)
        self.entropy_estimate = 0
        self.min_entropy = min_entropy
        
    def _mix_pool_bytes(self, bytes):
        raise NotImplementedException()

    def _increase_estimate(self, n_bits):
        raise NotImplementedException()

    def _decrease_estimate(self, n_bits):
        raise NotImplementedException()

    def debit_randomness(self):
        if (self.entropy_estimate > self.min_entropy):
            self._decrease_estimate(pool_size * 8)
            hashed = hash(self.pool)
            self._mix_pool_bytes(hashed)
            return hashed
        else:
            return None
            
    def credit_randomness(self, value):
        self._mix_pool_bytes(value)
        self._increase_estimate(len(value) * 8)

class SimpleEntropyPool(EntropyPoolBase):
    def _mix_pool_bytes(self, bytes):
        sha256 = hashlib.sha256()
        sha256.update(bytes)
        sha256.update(self.pool)
        self.pool = bytearray(sha256.digest())

    def _increase_estimate(self, n_bits):
        self.entropy_estimate += n_bits

    def _decrease_estimate(self, n_bits):
        self.entropy_estimate -= n_bits
        
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

        pool = SimpleEntropyPool(10)
        print("Entropy pool {}".format(pool))

        print("Adding integers to pool...")
        for i in range(20):
            print("I: {}".format(i))
            pool.credit_randomness(bytes(i))

        print("Debiting randomness")
        print(pool.debit_randomness())
        
    else:
        print("Unexpected input")        
