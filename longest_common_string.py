x = "CGATAATTGAGA" 
y = "GTTCCTAATA"
cls={}
clss=""
for i in range(-1,len(x)):
    cls[(i,-1)] = 0
for j in range(-1,len(y)):
    cls[(-1,j)] = 0
    
for i in range(0,len(x)):
    for j in range(0,len(y)):
        if x[i] == y[j]:
            clss=clss+x[i]
            cls[(i,j)] = cls[(i-1,j-1)]+1
        else:
            cls[(i,j)] = max(cls[(i-1,j)],cls[(i,j-1)])
print(cls)
