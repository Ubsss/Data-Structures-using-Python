# Given Gary's sequence of up and down steps during his last hike,
# find and print the number of valleys he walked through.
#
# For example. given s = "UDDDUDUU" your code should return 1.

s = "UDDDUDUU"
s2 = "DDUUDDUDUUUD"



# find when count come from negative to 0 and increment valleys
# This is just conting pairs of 0s!!!!

# TC 0(n) & SC 0(1)
def counting_valleys(string):
    count = 0
    valleys = 0

    for i in string:
        if i == "U":
            count += 1
        elif i == "D":
            count -= 1

        # if we just came up from see level
        if count == 0 and i == "U":
            valleys += 1

    return valleys


print(" There are %s valleys in this string. " % counting_valleys(s2))