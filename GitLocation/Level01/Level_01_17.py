# 다음 함수에서 에러가 발생하는 이유 : 기본값을 갖고 있는 인자 다음에는 반드시 기본값을 갖는 인자가 나와야 함
# 원본
#def greet(msg="Good Morinig!", name):
#    return "Hi! " + name + ', ' + msg

# 다음과 같이 수정
def greet(name, msg="Good Morinig!"):
    return "Hi! " + name + ', ' + msg

def greet1(msg="Good Morinig!", name="none"):
    return "Hi! " + name + ', ' + msg

def greet2(name, msg):
    return "Hi! " + name + ', ' + msg

# 함수 패킹 예제 - 패킹된 인자를 *(iterator 연산자)를 사용하여 반복사용
def add(*d):
    ret = 0
    for i in d:
        ret += i
    return ret

print(greet("Kim"))
print(greet("Park", "How do you do?"))

print(add(1, 5))
print(add(*(i for i in range(1, 11))))