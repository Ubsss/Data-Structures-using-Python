list = [4,3,1,2]

def minimum_swaps(arr):
    min = 0
    for k in range(len(arr) - 1, 0, -1):
        for j in range(k):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                min+=1

    print(arr)
    print(min)
    return

minimum_swaps(list)