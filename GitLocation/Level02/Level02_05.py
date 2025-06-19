
def makeListInList(target, num):
    ret = []
    for idx, value in enumerate(target):
        if idx % num == 0:
            ret.append(list(target[idx : idx + num]))

    return ret

def makeListInList2(target, num):
    return [list(target[idx : idx + num]) for idx, value in enumerate(target) if idx % num == 0]

x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(makeListInList(x, 5))
print(makeListInList2(x, 3))