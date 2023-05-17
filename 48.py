sum = 0
for i in range(1,1001):
    a = (i**i)
    sum = sum + a

string_sum = str(sum)
print(string_sum[-10:])

# The properties we want to exploit are

# (a*b) % c = ((a % c) * (b % c) )% c

# (a+b) % c = ((a % c) + (b % c) )% c.

result = 0
modulus = 10000000000
for i in range(0,1001):
    temp = i
    for j in range(1,i):
        temp *= i
        temp %= modulus
    result += temp
    result %= modulus

print(result)