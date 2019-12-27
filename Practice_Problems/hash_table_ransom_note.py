
magazine = ["give", "me", "one", "grand", "today", "night"]
note = ["give", "one", "grand", "today"]

def check_magazine(magazine, note):
    my_dict = {}
    for i in magazine:
        if i not in my_dict:
            my_dict[i] = 0
        my_dict[i] += 1
    for i in note:
        if i not in magazine:
            return "No"
        magazine[j] -= 1
    return "Yes"

print(check_magazine(magazine,note))