import math

def sum_of_divisors(k):
    sum=0
    for i in range(2,int(math.sqrt(k))+1):
        if k%i==0:
            sum = sum + i + k/i
    
    return sum + 1

n=1

answer = 0

while n<10000:
  if sum_of_divisors(sum_of_divisors(n)) == n and sum_of_divisors(n) != n: 
      print(n)
      #added because 6 follows above algorith but a!=b so is not an amicable number
      answer = answer + n
  n = n + 1
  
print("Answer is", answer)

# a = b for 1,6, 28, 496, 8128

