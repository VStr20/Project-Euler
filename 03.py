import math
def is_prime(k):
    for i in range(2,k):
        if(k%i == 0):
            return False
    return True

m = 600851475143
max = 0
for a in range(2,int(math.sqrt(m))+1):
    if(m%a == 0):
        if(is_prime(a) and max<a):
            max = a
        elif(is_prime(int(m/a)) and max<m/a):
            max = m/a

print(max)
