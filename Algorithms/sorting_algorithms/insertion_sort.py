arr = [2,1,6,4,3, 1]

#O(n^2)
def insertion_sort(array):
    for i in range(len(array)):
        temp = array[i]
        j = i

        while j>0 and temp<array[j-1]:
            array[j] = array[j-1]
            j = j - 1

        array[j] = temp
    return array

print(insertion_sort(arr))