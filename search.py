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

#DFS
def dfs(a,v,x):
    print("visited", visited)
    print("visiting",v)
    if a[v] == x:
        return v , a[v]
    visited.add(v)
    for e in edgesOf(v):
        print("exploring",e, "explored", explored)
        if(e not in explored):
            explored.add(e)
            u,w = e.split("-")
            if(int(w) not in visited):
                print("discover edge:",e)
                r = dfs(a,int(w),x)
                if(r != None):
                    return r
            else:
                print("back track edge:",e)

def edgesOf(v) -> set:
    myedges:set=set()
    if(v!=0):
        if(v%2==0):
            myedges.add(str(v//2-1)+"-"+str(v))
        else:
           myedges.add(str(v//2)+"-"+str(v)) 
    if 2*v+1 < len(a):
        myedges.add(str(v)+"-"+str(2*v+1))
    if 2*v+2 < len(a):
        myedges.add(str(v)+"-"+str(2*v+2))
    print("edges of", v, myedges)
    return myedges
    
    
    
a = [2, 3, 3, 3, 4, 5, 5, 5, 7, 323, 56435,8]
for x in reversed(a):
    visited:set = set()
    explored:set = set()
    print("search: ", x," return: ",dfs(a,0,x), a,"\n")
print("search: ", 30," return: ",dfs(a,0,30), a)
    explored:set = set()
    print("search: ", x," return: ",dfs(a,0,x), a)
print("search: ", 30," return: ",dfs(a,0,30), a)

#DFS stack
def dfs(a,v,x):
    stack = []
    stack.append(v)
    while stack :
        print("stack", stack)
        u = stack.pop()
        print("visited", visited)
        print("visiting", u)
        visited.add(u)
        edges = edgesOf(u)
        for e in edges:
            m, n = e.split("-")
            j=int(n)
            if(int(j) not in visited):
                if a[j] == x:
                    return j, a[j]
                stack.append(j)

def edgesOf(v) -> set:
    myedges:set=set() 
    if 2*v+1 < len(a):
        myedges.add(str(v)+"-"+str(2*v+1))
    if 2*v+2 < len(a):
        myedges.add(str(v)+"-"+str(2*v+2))
    print("edges of", v, myedges)
    return myedges
    
    
    
a = [2, 3, 3, 3, 4, 5, 5, 5, 7, 323, 56435,8]
for x in reversed(a):
    visited:set = set()
    explored:set = set()
    print("search: ", x," return: ",dfs(a,0,x), a,"\n")
print("search: ", 30," return: ",dfs(a,0,30), a)
