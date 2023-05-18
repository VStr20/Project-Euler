# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

def is_prime(a):
    for i in range(2, a):
            if(a%i == 0):
                return False
    return True

primenumbers = [2]
for k in range(3, 1000, 2):
    if(is_prime(k)):
        primenumbers.append(k)

def num_contains_even(b):
    for p in str(b):
        if(int(p)%2 == 0):
            return True
    return False

prime = []
prime1 = []
sum_ans = 0
answer = 0
for num in range(11, 1000, 2):
    count = 1
    temp = num
    if(num_contains_even(num)):
        continue
    else:
        if num in prime:
            continue
        else:
            if temp in primenumbers:
                for m in range(0, len(str(num))-1):
                    temp = (temp%10)*(10**(len(str(num))-1)) + int(temp/10)
                    if temp in primenumbers:
                        count += 1

            if(count == len(str(num))):
                answer += 1
                prime1.append(num)
                for m in range(0, len(str(num))):
                    temp = (temp%10)*(10**(len(str(num))-1)) + int(temp/10)
                prime.append(temp)

x=list(set(prime)|set(prime1))
print(sorted(x))
print(len(x)+4)    # +4 for including numbers 2, 3, 5, 7

# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 31
# 37
# 71
# 73
# 79
# 97
# 113
# 131
# 197
# 199
# 311
# 337
# 373
# 719
# 733
# 919
# 971
# 991
# 1193
# 1931
# 3119
# 3779
# 7793
# 7937
# 9311
# 9377
# 11939
# 19391
# 19937
# 37199
# 39119
# 71993
# 91193
# 93719
# 93911
# 99371
# 193939
# 199933
# 319993
# 331999
# 391939
# 393919
# 919393
# 933199
# 939193
# 939391
# 993319
# 999331