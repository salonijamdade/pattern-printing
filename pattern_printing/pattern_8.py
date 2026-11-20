n=5
spc=0
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for s in range(0,i*2-1):
        print("*",end="")
    print()
    spc+=1