for t in range(1,7,1):
    for r in range(7,t,-1):
        print(" ",end=" ")
    for g in range(t,0,-1):
        print(g,end=" ")
    for w in range(2,r,1):
        print(w,end=" ")
    print()

