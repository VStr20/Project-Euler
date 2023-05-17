t = 200
r_ways = [1] + [0] * t
print("Length is", len(r_ways))
for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(len(r_ways) - coin):
        r_ways[i + coin] += r_ways[i]
    print(str(r_ways[len(r_ways)-1]))

num =  123456789
k = ('0')
for m in str(num):
    k = k + str(m)

print(k)