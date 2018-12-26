#O(n2)-O(n logn)
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quick_sort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)

        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

    return arr

list = [17,34,1,8,0,23,7]

print(quick_sort(list,0,(len(list)-1)))