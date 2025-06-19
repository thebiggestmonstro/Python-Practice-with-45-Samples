import os

def readFiles(filespath):
    ret = []
    if os.path.exists(filespath):
        for file in os.listdir(filespath):
            with open(f"{filespath + file}", 'r') as f:
                ret.append(f.read().replace("\n", ""))
    return ret

import glob

def readFiles2(filespath):
    ret = []
    if os.path.exists(filespath):
        for file in glob.glob(filespath + '\*.txt'):
            with open(f"{file}", 'r') as f:
                ret.append(f.read().strip("\n"))
    return ret

print(readFiles("Resource/"))
print(readFiles2("Resource"))