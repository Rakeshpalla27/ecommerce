
"""

write a fun which states two parameters a,b type caste the value of second arguement into integerthen mutliply both the arguements a
print the last didgit of the result
psoitional 
keyword (b=10)//parameters
default (b="raki")//arguemnts
unknown 

positional:

def func(a,b):
    a=int(a)
    b=int(b)
    c=a*b
    print(c%10)


a,b=map(float,input().split())
func(a,b)

keyword:

def func(a,b):
    print(b)
s,f=map(int,input().split())
func(b=f,a=s)



default :
def defa(a=5,b=10):
    print(a+b)
a,b=map(int,input().split())
defa()
defa(a,b)



def func(**name):
    print("name",name["lname"])
func(fname="pras",lname="jha",)

cal sum of first n last digits of a no
def func(no):
    n=no%10
    while no>=10:
        no=no//10
    l=no%10
    print(l+n)
for i in range(2):
    a=int(input())
    func(a)
    write a log func which accepts the user only when displace the msg log successlfuly and keeps asking who 
     enter the credentials untill they are crt """
# def func():
#     while(True):
#         name1=input("name")
#         pass1=input("pass")
#         if name1==pass1:
#             print("successfull")
#             break
        
#         else:
#             continue
# func()

#recurrense realtion -n*n-1!
#base case-when to stop o!=1
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# def fab(n):
#     if n==0:
#         print("enter valid no")
#     if n==1:
#         print("0")
#     if n==2:
#         print("0 1")
#     else:
#         fac(n,0,1)
# fac()
# """wirte the recursive program to print the digits of a no in reverse order"""
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         res=n%10
#         print(res,end=" ")
#         n//=10
#         fact(n)
# fact(120)
# def nat(n):
#     if n<0:
#         return 1
#     print(abs(n-10))
#     n-=1
#     nat(n)
    
# nat(10)
# write a recursive fun to count the no of digits of a no
# write a rec fun to cal the sum of digits of a sum
# def no(n):
#     if n==0:
#         return 0
    
#     return 1+ no(n//10)
    
# a=no(7569)
# print(a)
# def no(n):
#     if n==0:
#         return 0
#     else:
#         return 1+no(n//10)
# def co(b,c):
#     if b==0:
#         return 0
#     else:
#         temp = b%10
#         return pow(temp,c) +co(b//10,c)
# z=int(input())
# a=no(z)
# am=co(153,a)
# if am==z:
#     print("yes")
# else:
#     print("no")



