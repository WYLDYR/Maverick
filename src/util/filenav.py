import os

def displayPath(path):

    pathResult = os.listdir(path)

    for item in pathResult:
        print(item)