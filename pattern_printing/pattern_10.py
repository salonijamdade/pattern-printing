n=5
spc=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1: #this will print stars at last and first row 
            print("*",end=" ")
        elif j==0 or j==n-1: #this will print stars at last and first column
            print("*",end=" ")
        else:                #this will print spaces when not stars
            print(" ",end=" ")
    print()
