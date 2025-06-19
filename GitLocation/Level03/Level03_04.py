
while(True):
    pw = input()
    res = []

    if not any(i.isdigit() for i in pw):
        res.append("최소 하나의 숫자가 포함되야 합니다")
    if not any(i.isupper() for i in pw):
        res.append("최소 하나의 대문자가 포함되야 합니다")
    if len(pw) < 8:
        res.append("비밀번호의 길이는 8자 이상이어야 합니다")

    if len(res) == 0:
        print("비밀번호 형식이 맞습니다")
    else:
        for i in res:
            print(i)
