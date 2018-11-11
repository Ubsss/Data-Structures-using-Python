array = [2,8,4,2,3,1,9,19,14]

# O(n^2)
def selection_sort(array):
    for fill_slot in range(len(array) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if array[location] > array[position_of_max]:
                position_of_max = location

        temp = array[fill_slot]
        array[fill_slot] = array[position_of_max]
        array[position_of_max] = temp

    return array

print(selection_sort(array))