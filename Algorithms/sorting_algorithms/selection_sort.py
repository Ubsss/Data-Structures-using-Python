array = [2,8,4,2,3,1,9,19,14]

# O(n^2)
def selection_sort(arr):
    for i in range(len(arr)):
        min_pos = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j

        temp = arr[i]
        arr[i] = arr[min_pos]
        arr[min_pos] = temp

        print(arr)

    return arr

print(selection_sort(array))