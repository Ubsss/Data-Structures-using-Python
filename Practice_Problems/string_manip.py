text = "hello there"
pal = "madamsmad"

# TC = O(n)
# SC = O(n)
def reverse_string_1(s):
  str = ""
  for i in s:
    str = i + str
  return str

# TC = O(n)
# SC = O(n)
def reverse_string_2(s):
    return s[::-1]

# ************************************
"""""
starting from the left, check each sequential combination of substrings
in the string to see if it is a pal
"""""
# TC = O(n)
# SC = O(n)
def pal_check(s):
    new_str = s[::-1]
    if new_str == s:
        return True
    return False

def longest_pal_subsequence(s):
    count = 0
    real_subsequ = ""
    for j in range(0,len(s)-1):
        for i in range(j, len(s)):
            sub_seq = s[j:i+1]
            if pal_check(sub_seq) == True:
                if len(sub_seq) > count:
                    count = len(sub_seq)
                    real_subsequ = sub_seq
    return count, real_subsequ

print(longest_pal_subsequence(pal))