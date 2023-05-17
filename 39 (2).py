max_p = 0
max_count = 0
p = 4

while(p<=1000):
    counter = 0
    for m in range(0,int(p/2)):
        for k in range(0,int(p/2)):
            if(m == int((p*(p-2*k))/(2*(p-k)))):
                counter += 1

    if(max_count<counter):
        max_count = counter
        max_p = p
    else:
        continue 
    p += 1

print(max_p, max_count)