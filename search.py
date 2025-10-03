#BinarySearch
a = [2, 3, 3, 3, 4, 5, 5, 5, 7, 323, 56435]
def binarySearch(a,x) -> int|None : 
    k=len(a)//2
    print(f"{x} [{k}] {a[k]}")
    if(x == a[k]):
        return k
    elif k==0:
        return None
    elif(x < a[k]):
        print(a[:k])
        return binarySearch(a[:k],x)
    else:
        print(a[k+1:])
        j = binarySearch(a[k+1:],x)
        if(j==None):
            return None
        else:
            return k+1 + binarySearch(a[k+1:],x) 
for x in a:     
 print("search: ", x," return: ",binarySearch(a, x), a)
print("search: ", 30," return: ",binarySearch(a, 30), a)
