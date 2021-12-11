import sys

temp = [0] * 100000

def merge(arr,first,middle,last):
    i = first
    j = middle
    k = first 
    count = 0

    while i<middle and j<=last:
        if arr[i]<=arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1
            count += middle-i

    while i<middle:
        temp[k] = arr[i]
        i += 1
        k += 1 
    while j<=last:
        temp[k] = arr[j]
        j += 1 
        k += 1

    while first<=last:
        arr[first] = temp[first]
        first += 1

    return count

def mergeSort(arr,first,last):
    count = 0
    if first<last:
        middle = (first+last)//2
        count += mergeSort(arr,first,middle)
        count += mergeSort(arr,middle+1,last)
        count += merge(arr,first,middle+1,last)
    return count

#Swap count using merge sort   
def swapCount(arr):
    count = sys.maxsize
    for i in range(len(arr)-1):
        print(arr,mergeSort(arr[::],0,len(arr)-1))
        arr = list(arr[len(arr)-1])+arr[0:len(arr)-1]
        count = min(count,mergeSort(arr[::],0,len(arr)-1))
    return count

#Optimised approach
def swapCount(arr):
    rot = 0
    mid = (len(arr)-1)//2
    c = 0
    itr = 1
    prev = 0
    for i in arr[mid+1:][::-1]:
        for j in arr[0:mid+1]:
            if i<j:
                c += 1
            else:
                c -= 1
        if c>prev:
            rot = itr
        itr += 1
        prev = c
    arr = list(arr[len(arr)-rot:])+arr[0:len(arr)-rot]
    count = mergeSort(arr[::],0,len(arr)-1)
    return count

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
count = swapCount(arr)
print(count)

