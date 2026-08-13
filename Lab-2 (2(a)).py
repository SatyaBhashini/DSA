def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1

n = int(input("Enter no. of elements:"))
arr=[]
print("Enter the elements:")

if arr==sorted(arr):
    print("\n The input list is already sorted.")
else:
    print("\n The input list is not sorted.")
    print("Sorting the list...")
    arr.sort()
print("Sorted list.",arr)

for i in range(n):
    arr.append(int(input()))
    
key=int(input("Enter element to search:"))
result=binary_search(arr,key)
if result!=-1:
    print("Element found at index",result)
else:
    print("Element not found.")
        
