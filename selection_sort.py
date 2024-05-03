A = [64, 25, 12, 22, 11]

for i in range(len(A)-1):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[j] < A[min_idx]:
            min_idx = j
    A[i], A[min_idx] =  A[min_idx], A[i] 



print ("Sorted array")
for i in range(len(A)):
    print(A[i],end=" ") 


#Memory complexity O(1)
#Time complexity O(n^2)