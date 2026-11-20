n=5
spc=5
for i in range(1,n+1): #this will run for how many times rows we want
    for j in range(n-i): # this will print how many time space should be printed.ex-(5-1)=4 these many times space will be printed
        print(" ",end=" ")
    for s in range(i):
        print("*",end=" ") #this will print * i times 
    print()
