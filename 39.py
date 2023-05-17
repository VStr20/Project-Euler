import math
from collections import Counter
import time
from statistics import mode

start = time.time()

# solution = []

# for a in range(1,500):
#     for b in range(1,500):
#         c = math.sqrt(a**2 + b**2)
#         if(int(c) == c and a + b + c <=1000):
#             solution.append(a+b+c)


# p = Counter(solution)
# q = mode(solution)
# print(q)
# print(p.most_common(1)[0])

max_solution = 0
max_p = 0
for p in range(1,1001):
    solution=0
    for a in range(2,500):
        for b in range(2,500):
            # if(a*a + b*b == (p - a - b)**2):
            if(p*(p-2*a) % 2*(p-a) == 0):
                solution = solution + 1
    if(max_solution<solution):
        max_solution = solution
        max_p = p
    print(p, " ", max_solution)

print(max_solution)
print(max_p)

end = time.time()

print(end - start)