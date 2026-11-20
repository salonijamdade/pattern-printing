n=5
spc=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for s in range(i):
        print("*",end=" ")
    print()


    # for j in range(5,0,-1):
    #     print(" ",end=" ")
    # for s in range(n,s+1):
    #     print("*",end=" ")
    # # print("*",end=" ")
    # print()