d = {
    "group1" : [
        {'name' : 'Park', 'age' : '32', 'gender' : 'Male'},
        {'name' : 'Cho', 'age' : '30', 'gender' : 'Feale'},
        {'name' : 'Kwon', 'age' : '39', 'gender' : 'Male', 'married' : 'No'}
    ],
    "group2" : [
        {'name' : 'Kang', 'age' : '31', 'gender' : 'Male', 'married' : 'No'},
        {'name' : 'Lee', 'age' : '37', 'gender' : 'Female', 'married' : 'Yes'}
    ],
    "type" : {'a' : 'employee', 'b' : 'officer', 'c' : 'director', 'd' : 'manager', 'e' : 'service provider'}
}

import json

# 단순 출력만 하는 경우 json 라이브러리의 dumps 메서드를 사용한다
# 인자로 사용한 indent 인자를 사용하면 지정한 값만큼 들여쓰기가 되어 보기 쉬워진다

print(json.dumps(d, indent=2))

# json 파일로 저장하고 싶다면 json 라이브러리의 dump 메서드를 사용한다
with open('tmp.json', 'w') as f :
    json.dump(d, f, indent=2)
