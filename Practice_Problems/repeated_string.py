# Given an integer, n, find and print the number of letter
# a's in the first n letters of the string.
#
# For example, if the string s='abcac' and n = 10, the substring we consider
# is 'abcacabcac', the first 10 characters of the string. There are 4 occurrences
# of a in the substring.

string = "abcacaca"

def print_string(s,n):
    print(s.count("a")*(n//len(s)) + s[:n % len(s)].count("a"))

print_string(string, 10)