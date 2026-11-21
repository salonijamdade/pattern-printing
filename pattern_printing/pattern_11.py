n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")  #(i==1) will print * at first row ,(i==n) this will print stars at last row
        else:                   #(j==1)this will print stars on the left side,(j==i) will print slop which will be equal to i
            print(" ",end=" ")
    print()
