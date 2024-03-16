"""n=12345
while(n>0):
    res=n%10
    print(res)
    n//=10


n=12345
c=0
while(n>0):
    res=n%10
    c+=1
    n//=10
print(c)


sum=0
n=12345
while(n>0):
    res=n%10
    sum+=res
    n//=10
print(sum)

fac=1
n=12345
while(n>0):
    res=n%10
    fac*=res
    n//=10
print(fac)"""

"""take an integer as input and check whether if the no is divisible by sum of digits or not
a=int(input("no"))
n=a
sum=0
while(a>0):
    res=a%10
    sum=sum+res
    a=a//10
if(n%sum==0):
    print("yes")
else:
    print("no")

take a input check if the sum of factors of that no is >original no or not
a=int(input("no:"))
n=a
sum=0
for i in range(1,a):
    if(a%i==0):
        sum+=i
if(sum>n):
    print("yes")
else:
    print("no")


palendrom
n=int(input("enter no:"))
a=n
nn=0
while(n>0):
    res=n%10
    nn=nn*10+res
    n=n//10 
if nn==a:
    print("yes")
else:
    print("no")"""

"""di=0
notdi=0
for i in range(1,31):
    if i%6==0:
        di+=i
    else:
        notdi+=i
a=di-notdi
print(abs(a))"""

"""amstrong no"""
a=int(input("enter no"))
n=a
am=0
count=0
while(a>0):
    count+=1
    a=a//10
print(count)
a=n
while(count>0):
    while(a>0):
        res=a%10
        am+=res**count
        a=a//10
    count-=1
print(am)
    
    

    


