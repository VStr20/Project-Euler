# d1d2d3d4d5d6d7d8d9d10
import time
start = time.time()

from itertools import permutations

p = permutations('0123456789')

solution = 0

for i in p:
    if(int(i[3])%2 == 0):
        if(int(i[5])%5 == 0):
            if((int(i[3])+int(i[4])+int(i[2]))%3 == 0):
                if((2*int(i[4])+3*int(i[5])+int(i[6]))%7 == 0):
                    if((int(i[5])+int(i[7])-int(i[6]))%11 == 0):
                        if((10*int(i[6])+int(i[7])+4*int(i[8]))%13 == 0):
                            if((10*int(i[7])+int(i[8])-5*int(i[9]))%17 == 0):
                                solution += int(''.join(i[0:10]))
        
end = time.time()
print(solution)
print(end - start)