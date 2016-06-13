#! /usr/bin/env python3

import sys

import entropy
import hashlib
import binascii
import time

pool_size = 256

def hash(x):
    return hashlib.sha256(bytearray(hashlib.sha256(x).digest())).digest()

# TODO: Crediting and debiting from the entropy pool should be
#       thread safe.

# Base class for constructing an entropy pool
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

    # Debit random bits from the entropy pool and adjust the entropy
    # estimate
    def debit_randomness(self):
        if (self.entropy_estimate > self.min_entropy):
            self._decrease_estimate(pool_size * 8)
            hashed = hash(self.pool)
            self._mix_pool_bytes(hashed)
            return hashed
        else:
            return None

    # Credit random bits to the entropy pool and adjust the entropy
    # estimate
    def credit_randomness(self, value):
        self._mix_pool_bytes(value)
        self._increase_estimate(len(value) * 8)

# Simple implementation of entropy pool with naive implementations
# for mixing the entropy pool and updating the estimates of the
# entropy in the pool
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

def credit_all_randomness(pool):
    read_count = entropy.read_count()
    write_count = entropy.write_count()

    # TODO: Network IO functions block sometimes.
    # Figure out why
    # bytes_sent = entropy.bytes_sent()
    # bytes_recv = entropy.bytes_recv()
    
    interrupts_count = entropy.interrupts_count()
    ctx_switches = entropy.ctx_switches()

    sources = [
        read_count,
        write_count,
        # bytes_sent,
        # bytes_recv,
        interrupts_count,
        ctx_switches
    ]

    for source in sources:
        pool.credit_randomness(bytes(source))
        
if __name__ == '__main__':

    if len(sys.argv) == 1:
        pool = SimpleEntropyPool(100)
        try:
            while True:
                blob = pool.debit_randomness()
                if(blob == None):
                    time.sleep(0.5)
                    credit_all_randomness(pool)
                else:
                    print(blob.decode('ascii', errors="ignore"), end="")
        except KeyboardInterrupt:
            pass

    elif (sys.argv[1] == "test"):
        print("*********************")
        print("    Testing stats")
        print("*********************")
        
 
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
            pool.credit_randomness(bytes(i))

        print("Debiting randomness")
        print(pool.debit_randomness())
        
    else:
        print("Unexpected input")        
