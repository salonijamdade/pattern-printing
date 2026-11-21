n=5
spc=5
for i in range(1,n+1): # i times it will iterate rows
    for j in range(n-i): # j times it will print spaces 
        print(end=" ")
    for s in range(0,i*2-1): # incrementing the stars by multiplaying  by 2 and minus 1
        print("*",end="")
    print()
    spc-=1 # decrementing the spaces 

m=4
sp=0
for i in range(m,0,-1): # this will start from 5 4 3 2 1
    for j in range(n-i): # this will print spaces by n-i
        print(end=" ")
    for s in range(0,i*2-1): # this will calculate how many stars to print 
        print("*",end="")
    print()
    sp+=1 #increment spc counter