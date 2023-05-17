number = []

for i in range(0,1000000):
    for x in str(i):
        number.append(int(x))

answer = 1
for p in range(0,7):
    answer = answer*(number[(10**p)])
    print(number[(10**p)], answer)

print(answer)