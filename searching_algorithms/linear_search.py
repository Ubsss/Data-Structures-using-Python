array = [1,2,3,4,5,1, 6,7,8,9,10]

# O(n)
def linear_search(array, key):
    indexies = []

    for i in range(len(array)):
        if array[i] == key:
            print(i)

    return indexies

linear_search(array, 1)

