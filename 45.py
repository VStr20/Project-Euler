import time
import math

start = time.time()

triangular = []
pentagonal = []
hexagonal = []

for i in range(0,100000000):
    triangular.append(i*(i+1)/2)
    pentagonal.append(i*(3*i-1)/2)

# for i = 2*m - 1 triangular number is hexagonal number

for a in range(len(triangular)):
    if(a%2 != 0): #check is number is hexagonal
        if(triangular[a] in pentagonal):  #check if number is pentagonl
            if(int(math.sqrt(triangular(a))) == math.sqrt(triangular[a])): #check if number is
                print(int(a*(a+1)/2))

end = time.time()

print(end - start)