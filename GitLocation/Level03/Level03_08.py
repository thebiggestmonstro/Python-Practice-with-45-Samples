import os

def findFilesWithSubFolder(filepath):
    txtList = []
    pngList = []

    if os.path.exists(filepath):
        for root, subfolder, files in os.walk(filepath):
            for file in files:
                if ".txt" in file or ".TXT" in file:
                    txtList.append(file)
                elif ".png" in file or ".PNG" in file:
                    pngList.append(file)

    print(f"TXT file info : {txtList} Count : {len(txtList)}")
    print(f"PNG file info : {pngList} Count : {len(pngList)}")

import glob

def findFilesWithSubFolder2(filepath):
    txtList = []
    pngList = []

    if os.path.exists(filepath):
        txtList = [os.path.basename(filepath) for filepath in glob.glob(f"{filepath}/**/*.txt", recursive=True)
                   if os.path.isfile(filepath)]
        pngList = [os.path.basename(filepath) for filepath in glob.glob(f"{filepath}/**/*.png", recursive=True)
                   if os.path.isfile(filepath)]

    print(f"TXT file info : {txtList} Count : {len(txtList)}")
    print(f"PNG file info : {pngList} Count : {len(pngList)}")

findFilesWithSubFolder("TargetFolder_02")
findFilesWithSubFolder2("TargetFolder_02")