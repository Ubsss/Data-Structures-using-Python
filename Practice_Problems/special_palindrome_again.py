
string = "abracadabraar"
string2 = "ra"

def palendrome(string):

    rev_string = reversed(string)

    if list(string) == list(rev_string):
        return True
    return False

def substring_repeat_in_string(string, substring):
    rev_string = reversed(substring)
    return string.count(substring) + string.count(rev_string)

def first_repeating_aphabet(string):
    dictionary = {}
    for char in string:
        if char not in dictionary:
            dictionary[char] = 0
        dictionary[char] += 1

        if dictionary[char] == 2:
            print("%s is the first repeating character in string"%char)
            return


first_repeating_aphabet(string)
