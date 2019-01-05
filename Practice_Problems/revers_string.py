# O(n), O(1)
def rev_str(str):
    list1 = list(str)
    rev_list = list1[:]
    j = 0

    for i in range(len(list1)-1,-1,-1):
        rev_list[j] = list1[i]
        j += 1

    rev_list = ("").join(rev_list)

    return rev_list

string = "hi there"

print(rev_str(string))