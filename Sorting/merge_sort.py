# Merge sort is a simple & efficient algorithm that uses the
# divide and conquer approach. 
# 1. Recursively sort the left half of the input array
# 2. Recursively sort the right half of the input array
# 3. Merge two sorted sub arrays into one.

def mergeSort(A):
    # base case if the input array is one or zero just return:
    if len(A) > 1:
        # splitting input array
        print('splitting ', A)
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        # recursive calls to mergeSort for left and right sub arrays
        mergeSort(left)
        mergeSort(right)
        # initialize pointers for left (i) right (j) and output array (k)

        # 3 initialization operations
        i = j = k = 0
        # Traverse and merges the sorted arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i+=1
            else:
                A[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            A[k]=left[i]
            i+=1
            k+=1
        
        while j < len(right):
            A[k] = right[j]
            j+=1
            k+=1
        print('merging ', A)
        return A

if __name__ == "__main__":
    from random import seed 
    from random import randint 
    seed(1)

    #mergeSort([356, 97, 846, 251])

    mergeSort([randint(1,100000) for i in range(1000)])
