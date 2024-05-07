
def insertionSort(arr):
    for i in range(0,len(arr)-1):
        print(arr)
        print(i)
        j = i
        val = arr[j+1]
        while j >= 0 and val < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = val
arr = [12, 11, 13, 5, 6,7,33]
insertionSort(arr)
print("________________")
print(arr)


#time complexity: O(n^2)