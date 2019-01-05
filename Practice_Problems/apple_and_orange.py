def apples_and_oranges(s,t,a,b, apples, oranges):
    app_in_range = 0
    or_in_range = 0

    for i in range(len(apples)):
        if (a + (apples[i])) >= s and (a + (apples[i])) <=t:
            app_in_range += 1

    for j in range(len(oranges)):
        if  (b + (oranges[j]))  >= s and (b + (oranges[j])) <=t:
            or_in_range += 1

    print(app_in_range)
    print(or_in_range)

list1 = [-2,2,1]
list2 = [5,-6]
apples_and_oranges(7,11,5,15,list1,list2)

# for i in range(list[3][0]):
#     print(i)
#
# for j in range(list[3][2]):
#     print(j)

