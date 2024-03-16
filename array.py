#selection sort
"""a=list(map(int,input().split()))
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

bubble sort
a=list(map(int,input().split()))
n=len(a)
temp=0
for i in range(n,0,-1):
    for j in range(1,i):
        if (a[j]<a[j-1]):
            a[j],a[j-1]=a[j-1],a[j]
print(a)
insertion sort
a=list(map(int,input().split()))
n=len(a)
for i in range(1,n):
    while(i>0):
        if a[i]<a[i-1]:
            a[i],a[i-1]=a[i-1],a[i]
        i-=1
print(a)

merge sort"""
def mergesort(b,l,h):
    if l<h: 
        m=(l+h)//2
        mergesort(b,l,m)
        mergesort(b,m+1,h)
        merge(b,l,m,h)
def merge(b,l,m,h):
    n1 = m - l + 1
    n2 = h - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = a[l + i]
    for j in range(0, n2):
        R[j] = a[m + 1 + j]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
a=list(map(int,input().split()))
n=len(a)
mergesort(a,0,n-1)
print(a)


        





