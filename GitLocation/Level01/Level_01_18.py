# 전역 변수 : 함수 내부가 아닌 외부에 정의되어 전체 범위를 갖는 변수
# 전역 변수의 변경, 수정이 필요한 경우 global 키워드 사용

# 전역변수 예제 1
x = 100

def test1():
    return x * 10
print(test1())
print(x)

# 전역변수 예제 2
y = 100

def test2():
    global y
    y *= 10
    return y

print(test2())
print(y)