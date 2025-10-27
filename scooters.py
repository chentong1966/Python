finish=23
scooters=[7,4,14]
finish=10
scooters=[]
finish=27
scooters=[15,7,3,10]
finish=87
scooters=[15,7,35, 76,3,10]

def solution(finish,scooters):
    c=False
    t=0
    l=0
    scooters=sorted(scooters)
    if scooters:
        d=scooters.pop(0)
    else:
        return l

    while t < finish:
        print(t,l,d,scooters)
        while d < t :
            print(scooters,d)
            if scooters:
                d=scooters.pop(0)
            else:
                print("scooters empty")
                return l
        if d+10 <= finish:
            l = l +10
            t = d + 10
        else:
            return l + finish - d
  
        print(t,l,d,scooters)

    return l

print(solution(finish,scooters))


# pop from sorted list and check

finish=23
scooters=[7,4,14]
finish=10
scooters=[]
finish=27
scooters=[15,7,3,10]
finish=85
scooters=[15,7,35, 76,3,10]

def solution(finish,scooters):
    t=0
    l=0
    scooters=sorted(scooters)
    while scooters:
        d=scooters.pop(0)
        if t <= d:
            if d+10 <= finish:
                l = l +10
                t = d + 10
            else:
                return l + finish - d
    return l

print(solution(finish,scooters))

# heapq

finish=23
scooters=[7,4,14]
finish=10
scooters=[]
finish=27
scooters=[15,7,3,10]
finish=85
scooters=[15,7,35, 76,3,13]

import heapq
def solution(finish,scooters):
    t=0
    l=0
    heapq.heapify(scooters)
    while scooters:
        d=heapq.heappop(scooters)
        if t <= d:
            if d+10 <= finish:
                l = l +10
                t = d + 10
            else:
                return l + finish - d
    return l

print(solution(finish,scooters))


# return walking distance

finish=23
scooters=[7,4,14]
finish=10
scooters=[]
finish=27
scooters=[15,7,3,10]
finish=95
scooters=[15,7,35, 76,3,13]

import heapq
def solution(finish,scooters):
    t=0
    w=0
    heapq.heapify(scooters)
    while scooters:
        d=heapq.heappop(scooters)
        if t <= d:
            w = w + d - t
            t = d + 10
    if t < finish:
        w = w + finish - t
    return w

print(solution(finish,scooters))
