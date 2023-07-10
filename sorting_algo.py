# #merge sort
# def mergesort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         l=arr[:mid]
#         r=arr[mid:]
#         mergesort(l)
#         mergesort(r)

#         i=j=k=0
#         while i<len(l) and j<len(r):
#             if l[i]>r[j]:
#                 arr[k]=r[j]
#                 j+=1
#             else:
#                 arr[k]=l[i]
#                 i+=1
#             k+=1
#         while i<len(l):
#             arr[k]=l[i]
#             i+=1
#             k+=1
#         while j<len(r):
#             arr[k]=r[j]
#             j+=1
#             k+=1
#     return arr

# nums=[5,42,6,6,7,8,2]
# print(mergesort(nums))

#quick sort
# def find_piv(arr,low,high):
#     pivot=arr[high]
#     i=low-1
#     for j in range(low,high):
#         if arr[j]<=pivot:
#             i+=1
#             arr[i],arr[j]=arr[j],arr[i]
#     arr[i+1],arr[high]=arr[high],arr[i+1]
#     return i+1
# def quicksort(arr,low,high):
#     if low<high:
#         piv=find_piv(arr,low,high)
#         quicksort(arr,low,piv-1)
#         quicksort(arr,piv+1,high)
    
# arr=[10,30,50,20,90,80,70]
# quicksort(arr,0,len(arr)-1)
# print(arr)

# heapsort
# def heapify(arr, N, i):
#     largest = i 
#     l = 2 * i + 1
#     r = 2 * i + 2 

#     if l < N and arr[largest] < arr[l]:
#         largest = l

#     if r < N and arr[largest] < arr[r]:
#         largest = r

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]

#     heapify(arr, N, largest)

# def heapSort(arr):
#     N = len(arr)
#     # Build a maxheap.
#     for i in range(N//2 - 1, -1, -1):
#         heapify(arr, N, i)
#     # One by one extract elements
#     for i in range(N-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i] # swap
#         heapify(arr, i, 0)

# counting sort
def countingSort(arr):
    size = len(arr)
    output = [0] * size

    # count array initialization
    count = [0] * 10

    # storing the count of each element
    for m in range(0, size):
        count[arr[m]] += 1

    # storing the cumulative count
    for m in range(1, 10):
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of
    # each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    # copy the output array back into the input array
    for m in range(0, size):
        arr[m] = output[m]

# example usage
data = [1, 4, 1, 2, 7, 5, 2]
countingSort(data)
print("Sorted Array: ")
print(data)
