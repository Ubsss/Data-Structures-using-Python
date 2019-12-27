"""""
Junior/Senior
Write a method that takes in and returns true if str is a palindrome.
Write a method that takes in two strings and returns true if the two strings are anagrams
Write a method that the prompts the user for an int and a string and returns true if the int is equal to the size of the string.
"""""
# 3 point questions!!!!!!!!!!!
# question 1:
# TC = O(n)
# SC = O(n)
def pal_check(s):
    new_str = s[::-1]
    if new_str == s:
        return True
    return False

# question 2:
# TC = O(n)
# SC = O(1)
def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    for i in s1:
        if i not in s2:
            return False
    return True

# question 3:
# TC = O(n)
# SC = O(1)
def int_string(numb,name):
    if len(name) != numb:
        return False
    return True
# 3 point questions!!!!!!!!!!!

# 7 point questions!!!!!!!!!
# question 2:
# TC = O(n)
# SC = O(1)
def add_array_sub_ods(arr):
    sum = 0
    odds = 0
    for i in arr:
        sum += i
        if i%2 != 0:
            odds += i
    return (sum - odds)

# 11 point questions!!!!!!!!!
# question 1:
# TC = O(n)
# SC = O(n)
def min_pairs(list):
    dup = 0
    incrementer = 0
    dict = {}

    for i in list:

        if list.count(i) > 1:
            if i not in dict:
                dict[incrementer] = i
                dup += 1

    return dup

print(31%11)