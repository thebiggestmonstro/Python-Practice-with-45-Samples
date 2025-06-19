
def sigma1(num):
    ret = 0
    for i in range(num+1):
        ret = ret + i
    return ret

def sigma2(num):
    return num * (num + 1) // 2

def sigma3(num):
    return sum(range(num+1))

print(sigma3(10))