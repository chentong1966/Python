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

#BinarySearch
def binarysearch(a, low, high, target):
    print(a, low, high, target)
    if low > high:
        return -1
    k=(low+high)//2
    if(a[k] == target):
        print(f"find {a[k]} at [{k}]")
        return k
    elif a[k] < target:
        return binarysearch(a, k + 1 , high, target)
    elif a[k] > target:
        return binarysearch(a, low , k-1, target)
        

a=[2, 3, 3, 3, 4, 5, 5, 5, 7, 323, 56435]
for x in a:     
 print("search: ", x," return: ",binarysearch(a, 0,len(a)-1,x), a)
print("search: ", 30," return: ",binarysearch(a, 0,len(a)-1,30), a)
