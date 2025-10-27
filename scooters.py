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
