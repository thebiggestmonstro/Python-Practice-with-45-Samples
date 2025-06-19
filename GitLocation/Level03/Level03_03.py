characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

import random

def genCode(n):
    code_list = []
    random.seed(None)

    while len(code_list) != n:
        chosen = random.sample(characters, 6)
        code = "".join(chosen)

        if code not in code_list:
            code_list.append(code)

    return code_list

print(genCode(3))
