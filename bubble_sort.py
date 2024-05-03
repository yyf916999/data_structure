
def bubbleSort(arr):
    for ind, v in enumerate(arr):
        for sub_ind in range(len(arr)-ind-1):
            print(arr)
            if arr[sub_ind] > arr[sub_ind+1]:
                sub_v = arr[sub_ind]
                arr[sub_ind] = arr[sub_ind+1]
                arr[sub_ind+1] = sub_v


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90, 101 ,1 ,2]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")


#O(1) Memory complexity
#O(n^2) Time complexity