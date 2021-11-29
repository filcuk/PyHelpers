import os
from os import walk
import fnmatch

# r- prefix causes string to be treated as literal 
userDir = r'C:\Users\FilipK'
downDir = userDir + r'\Downloads'
exprDir = userDir + r'C:\Users\FilipK\Desktop\Export\'
scrCapsDir = exprDir + r'\Screenshots'

scrCapsPattern = r'Screenshot ????-??-?? ??????.png'

f = []


for file in os.listdir(exprDir):
    if fnmatch.fnmatch(file, scrCapsPattern):
        f.extend(file)

print(f)



input()
