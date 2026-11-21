
n = 5

# Upper half
for i in range(1,n+1):
    for j in range(1,i+1):  # this will print * i times on left side
        print("*",end=" ")

    for m in range(2*(n-i)):  # this will print middle spaces
        print(" ",end=" ")

    for s in range(1,i+1):  # this will print * i times on right side
        print("*",end=" ")

    print()

# Lower half
for i in range(n-1,0,-1):
    for j in range(1,i+1):  # this will print * i times on left side
        print("*",end=" ")

    for m in range(2*(n-i)):  # this will print middle spaces
        print(" ",end=" ")

    for s in range(1,i+1):  # this will print * i times on right side
        print("*",end=" ")

    print()
