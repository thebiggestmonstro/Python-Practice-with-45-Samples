d = '''
    {"group1":[
                {'name': 'Park', 'age': '32', 'gender': 'Male'},
                {'name': 'Cho', 'age': '44', 'gender': 'Female'},
                {'name': 'Kang', 'age': '39', 'gender': 'Female', 'married': 'No'}
              ],
     "group2":[
                {'name': 'Kim', 'age': '23', 'gender': 'Male', 'married': 'Yes'},
                {'name': 'Lee', 'age': '37', 'gender': 'Male', 'married': 'No'}
              ],
     "type" : {"a": "employee", "b": "officer", "c": "director", "d": "manager", "e": "service provider"}
    }
    '''

import json

# 방법1 - loads를 사용, 스크립트 내부에서 json 파일을 가져오는 경우
result1 = json.loads(d.replace("'", "\""))

print(result1)
print(type(result1))

# 방법2 - load를 사용, 스크립트 외부에서 json 파일을 가져오는 경우
with open("./Target.json", "r") as out:
    result2 = json.load(out)
    print(result2)
    print(type(result2))