n=5
spc=5
for i in range(1,n+1): # i times it will iterate rows
    for j in range(n-i): # j times it will print spaces 
        print(end=" ")
    for s in range(0,i*2-1): # incrementing the stars by multiplaying  by 2 and minus 1
        print("*",end="")
    print()
    spc-=1 # decrementing the spaces 

