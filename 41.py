# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
# For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

import time

start = time.time()

primenumbers = []
def SieveOfEratosthenes(n):
  
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
  
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
  
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
  
    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primenumbers.append(p)
  
  
# Driver code
SieveOfEratosthenes(7654321)

from itertools import permutations
import functools

answer = []
p = permutations('1234567')

for m in p:
  # res = functools.reduce(lambda sub, ele: sub * 10 + ele, m)
  res = int(''.join(map(str, m)))   # convert tuple m to integer
  if(not ((res%10)%2 == 0 or res%10 == 5)):    # check for divisibility by 2 or 5
    if res in primenumbers:
      answer.append(res)
    else:
      continue
  else:
    continue

print(max(answer))

end = time.time()
print(end - start)

# Answer
# 14.469361305236816

# Hints
# Any 2, 3, 5, 6, 8, 9 digit pandigital number cannot be prime as its sum of digits is always divisible by 3
# Hence we check for 7 digit pandigital number
