# 다음의 동작은 string 라이브러리 import 후에, ascii_uppercase나 ascii_lowercase로도 가능하다

def makeFile():
    with open("ret.txt", 'w') as f:
        for i in range(65, 91):
            data = f"{chr(i)} "
            f.write(data)

makeFile()

import string

def makeFile2():
    with open("ret2.txt", 'w') as f:
        for i in string.ascii_uppercase:
            f.write(f"{i} ")

makeFile2()