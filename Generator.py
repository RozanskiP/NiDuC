from numpy import random

def generateBit(bits, m):
    for i in range(m):
        bits.append(random.randint(2))

    print(bits)