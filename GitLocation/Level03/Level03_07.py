import os

def defineFileExtensionName(filepath):
    pngList = []
    pyList = []

    if os.path.exists(filepath):
        for file in os.listdir(filepath):
            if ".py" in file or ".PY" in file:
                pyList.append(file)
            elif ".png" in file or ".PNG" in file:
                pngList.append(file)

    print(f"PNG file info : {pngList} Count : {len(pngList)}")
    print(f"Py file info : {pyList} Count : {len(pyList)}")

import glob

def defineFileExtensionName2(filepath):
    pngList = []
    pyList = []

    if os.path.exists(filepath):
        pyList = glob.glob1(filepath , '*.py')
        pngList = glob.glob1(filepath , '*.png')

    print(f"PNG file info : {pngList} Count : {len(pngList)}")
    print(f"Py file info : {pyList} Count : {len(pyList)}")

defineFileExtensionName("TargetFolder/")
defineFileExtensionName2("TargetFolder/")

