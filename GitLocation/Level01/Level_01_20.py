# 아래 함수의 실행 결과를 예측하라
def test(x, y):
    global a
    a = 49
    x,y = y,x
    b = 53
    b = 7
    c = 135
    print('Step1 : ', a, b, x, y)

a, b, x, y = 8, 13, 33, 44

test(23, 7)

print('Step2 : ', a, b, x, y)

# Step1 : 49, 7, 7, 23
# Step2 : 49, 13, 33, 44