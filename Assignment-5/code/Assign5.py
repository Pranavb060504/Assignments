import random
import numpy as np
from numpy.random import default_rng

def func(b):
    N = 100000
    rng = default_rng()
    arr = rng.choice([1, 0], size=(N,2), p=[b, 1-b])
    values, counts = np.unique(arr, return_counts=True, axis=0)
    #print(values)
    x1=counts[0] 
    #number of tosses where both coins result in tails
    x2=counts[1]
    #number of tosses where first coin results in tails and second results in heads
    x3=counts[2]
    #number of tosses where  first coin results in heads and second results in tails
    x4=counts[3]
    #number of tosses where both coins result in heads
    p=counts[0]+counts[1]+counts[2]+counts[3]
    print(counts[0]/p)
    print(counts[1]/p)
    print(counts[2]/p)
    print(counts[3]/p)
b=random.random()
#b=0.5
#b is the probability of getting heads in the coin
print(b)
func(b)
