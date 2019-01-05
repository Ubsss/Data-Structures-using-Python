
magazine = ["give", "me", "one", "grand", "today", "night"]
note = ["give", "one", "grand", "today"]


# tc = O(n^2)
# sc = O(1)
def check_magazine(magazine, note):
    count = 0
    for i in note:
        for j in magazine:
            if i == j:
                count += 1
                break
    if count == len(note):
        return "YES"
    else:
        return "NO"

print(check_magazine(magazine, note))