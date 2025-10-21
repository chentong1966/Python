import heapq
import sys
dist={("SFO","LAX"):337,("SFO","DFW"):1464,("SFO","ORD"):2704,("LAX","MIA"):2342,("ORD","DFW"):802,\
      ("ORD","BWI"):621,("BWI","MIA"):946,("BWI","JFK"):184,("JFK","PVD"):144,("JFK","BOS"):187}
c=[]
cities=[]
d={'BWI':0,'PVD':sys.maxsize,  'JFK':sys.maxsize,"SFO":sys.maxsize,"ORD":sys.maxsize,"LAX":sys.maxsize,"BOS":sys.maxsize,"MIA":sys.maxsize,"DFW":sys.maxsize}
pq=[]

def edgeOf(city):
    cityDict={}
    for cityPair, dd in dist.items():
        if city in cityPair:
           cityDict[cityPair] = dd
    return cityDict

def weightOf(newCity , city):
    if (newCity,city) in dist:
        return dist[(newCity,city)]
    elif (city,newCity) in dist:
        return dist[(city,newCity)]
    else:
        return sys.maxsize
    
for k,v in d.items():
    heapq.heappush(pq, (v, k))
    cities.append(k)
print(pq)

while pq :
    city = heapq.heappop(pq)[1]
    c.append(city)
    cities.remove(city)
    print("city",city)
    for newCity in cities:
        print("newCity",newCity)        
        dd = weightOf(newCity , city)
        print(newCity , city,"weight:",dd)
        if weightOf(newCity, city) + d[city] < d[newCity]:
            print("update d and pq",d[newCity] , newCity)
            pq.remove((d[newCity],newCity))
            d[newCity] = weightOf(newCity, city) + d[city]
            print(d)
            heapq.heappush(pq,(d[newCity] ,newCity))
            print(pq)
    
print(d)
print("city explored",c)
    
def otherCity(city,cityPair):
    a,b = cityPair
    if city == a:
        return b
    return a
def otherCity(city,cityPair):
    a,b = cityPair
    if city == a:
        return b
    return a    
