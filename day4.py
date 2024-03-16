#
# second smallest no 
# a=[-1,42,65,-4,6,22,-2,-5]
# min=0
# min2=0
# temp=0
# for i in range(0,len(a)):
#    if a[i]<a[min]:
#         min=i
# temp=a[min]
# print(temp)
# for i in range(0,len(a)):
#     if a[i]<a[min2] and a[i]!=a[min]:
#         min2=i
# print(a[min2])
# a=[-1,42,65,-4,6,22,-2,-5]
# min=0
# min2=0
# for i in range(len(a)):
#     if a[i]<a[min]:
#         min2=min
#         min=i
# print(a[min2])
# def rec(n):
#     if n==0:
#         return 
#     return 1+n%10
    
# print(rec(123))

# def rec(a,l):
#     if l==0:
#         return 
#     min=0
    
#     if a[l]<a[min]:
#         min=l
#     rec(a,l-1)
# a=[4,2,3,5]
# b=len(a)
# print(rec(a,b-1))
"""lamda function"""
# a=lambda x:x*2;print(a(2))
# "map fucntion"
# b=list(map(lambda x:x//10,[23,168,143]));print(b)
# a={1,2.5,6.7,"raki","hello",3,2,4}
# print(a)
# a.remove("raki")
# a.add("ramu")
# a.pop()
# print(a)

# "frozen set"
# fs={1,24,4}
# fs=frozenset(fs)
# print(fs)
"""000"""
# a=[2,0,1024,0,40,230,0]
# c=0
# b=[]
# for i in a:
#     if i==0:
#         c+=1
#     elif i!=0:
#         b.append(i)
# for i in range(c):
#     z=0
#     b.append(z)
# print(b)
# a=[2,0,1024,0,40,230,0]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]==0:
#             if a[j]!=0:
#                 temp=a[j]
#                 a[j]=a[i]
#                 a[i]=temp
# print(a)




