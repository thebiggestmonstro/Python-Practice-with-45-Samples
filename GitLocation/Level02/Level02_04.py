a = ["one", "two", "three", "four"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

# 방법 1
def makeDict(list1, list2, list3):
    dic = {}
    for idx, val in enumerate(list1):
        dic[val] = list2[idx] * list3[idx]

    return dic

# 방법 2
def makeDict2(list1, list2, list3):
    dic = {}
    for one, two, three in zip(list1, list2, list3):
        dic[one] = two * three

    return dic

# 방법 3
def makeDict3(list1, list2, list3):
    return {key : val1 * val2 for key, val1, val2 in zip(list1, list2, list3)}

# 방법 4
def makeDict4(list1, list2, list3):
    return dict((key, val1 * val2) for key, val1, val2 in zip(list1, list2, list3))

print(makeDict(a, b, c))
print(makeDict2(a, b, c))
print(makeDict3(a, b, c))
print(makeDict4(a, b, c))
