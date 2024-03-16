"""patterns"""

"""for i in range(1,5):
    if(i==2 or i==3):
        for j in range(1,5):
            if(j==2 or j==3):
                print(" ",end=" ")
            else:
                print("x",end=" ")
    else:
        for i in range(1,5):
            print("x",end=" ")
    print()"""
"""n=int(input("enter rows:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        for j in range(1,n+1):
            print("x",end=" ")
    else:
        for j in range(1,n+1):
            if(j==1 or j==n):
                print("x",end=" ")

            else:
                print(" ",end=" ")
    print()"""
"""for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""
"""for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()"""
"""count=1
for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for i in range(1,5):
    for j in range(5-i):
        print(5-i,end=" ")
    print()"""
"""for i in range(1,5):
    for s in range(4-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()"""

""" halo pyramid

n=5
for i in range(6):
    for j in range(n-i):
        print(" ",end=" ")
    for s in range(2*i-1):
        if s==0 or s==2*i-2:
            print("*",end=" ")
        else:
            if i==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()   """
"""n=5
for i in range(1,6):
    for j in range(n-):
        print(" ",end=" ")
    for s in range(2*i-1):
        if s==0 or s==2*i-2:
            print("*",end=" ")
        else:
            if i==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()"""
"""calcu the diff of sum of nos that are divisible by 6 and not divisible by 6in the  range of first 30"""
for i in range(6):
    for j in range(1,6-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(6):
    for j in range(i):
        print(" ",end=" ")
    for j in range(5,i,-1):
        print("*",end=" ")
    print()


    


        
        

