array = [1,2,3,4,5,6,7,8,9,10]

# # O(log n)
def binary_search(array, low_bound, hight_bound, key):
    while low_bound <= hight_bound:
        mid_bound = (low_bound + hight_bound)//2

        if array[mid_bound] < key:
            low_bound = mid_bound + 1
        elif array[mid_bound] > key:
            hight_bound = mid_bound - 1
        else:
            return mid_bound

    return -1

print(binary_search(array, 0, len(array) - 1, 11))