# a=list(map(int,input().split()))
# for i in range(8,10):
#     a.append(i)
# print(a)
# print(a[1:3])
# print(a[0::-1])
# for i in a:
#     print(f'loopaccess {i}',end=" ")
# a.insert(2,"raki")
# print(a)
# a.remove("raki")
# a=[["raki",1],["ramu",2]]
# print(a[0][1])
# a=[12,42,23,96,7,18,10,133]
# n=len(a)
# temp=0
# for i in range(n):
#     min=i
#     for j in range(i+1,n):
#         if a[j]<a[min]:
#             min=j
#     temp=a[i]
#     a[i]=a[min]
#     a[min]=temp
# print(a)
# f=a[0]
# l=a[-1]
# add=f+l
# sub=abs(f-l)
# a[-1]=add
# a[0]=sub
# print(a)
# a=(3,4,5,"raki")
# print(a[0:2])


# a=[-1,42,65,-4,6]
a=list(map(int,input().split()))
n=len(a)
temp=0
for i in range(n):
    min=i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min=j
    temp=a[i]
    a[i]=a[min]
    a[min]=temp
print(a)
a[0]
else:
    print("no negative no")