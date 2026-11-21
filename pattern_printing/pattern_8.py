n=5
spc=0
for i in range(n,0,-1):# this will start from 5 4 3 2 1
    for j in range(n-i): # this will print spaces by n-i
        print(end=" ")
    for s in range(0,i*2-1): # this will calculate how many stars to print 
        print("*",end="")
    print()
    spc+=1 #increment spc counter