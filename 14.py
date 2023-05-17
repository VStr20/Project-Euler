import numpy as np
import matplotlib.pyplot as plt
b=100     #change value of b for    more numbers
ab=np.arange(1,b,1)
s=0

def steps(k):
  s=0
  while k!=1:
    if k%2==0:
      k=k/2
      s+=1        
    else:
      k=3*k+1
      s+=1
  return s+1

pmax=0
a = [1]


for i in range(1,len(ab)):
  #print(type(i))
  p = steps(i)
  a.append(p)
  # append adds values p in rhe list a
  if pmax<=p:
      pmax=p
      
for j in range(1,b-1):
    if(steps(j)==pmax):
       print(j)

x = np.arange(1,b,1)
    
print(len(a),len(x))
#pylab.xlim([1,1000000])
#pylab.ylim([1,1000000])

#markerline, stemlines, baseline = plt.stem(steps(x), x, '-.')

#plt.show()

plt.stem(x, a, linefmt ='red', markerfmt ='-.', bottom = 1.1, use_line_collection = True)



      