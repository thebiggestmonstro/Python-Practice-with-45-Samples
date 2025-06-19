import os

def readText(filepath):
    ret = 0
    if os.path.exists(filepath):
        with open(f"{filepath}", 'r') as f:
            txt = f.read().split("\n")
            for i in txt:
                if i.startswith("C") == True:
                    ret += int(i.split(",")[1])

    return ret

print(readText("Target.txt"))