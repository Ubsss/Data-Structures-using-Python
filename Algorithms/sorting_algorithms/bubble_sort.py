my_list = [4,3,1,2]

# O(n^2)
def bubble_sort(array):
    for k in range(len(array) - 1, 0, -1):
        for j in range(k):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

