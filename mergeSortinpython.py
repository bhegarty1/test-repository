def mergeSort(arr):
    if(len(arr) > 1):
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(right)
        mergeSort(right)
        merge(left, right, arr)
        
def merge(left, right, arr):     
    leftL = len(left)
    rightL = len(right)
    i = 0
    j = 0
    k = 0

    while(i < leftL and j < rightL):
        if(left[i] < right[j]):
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while(i < leftL):
        arr[k] = left[i]
        i += 1
        k += 1
    while(j < rightL):
        arr[k] = right[j]
        j += 1
        k += 1

arr = [1,4,8,2,9,0,12,4,7]
print(arr)
mergeSort(arr)
print(arr)


