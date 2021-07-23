# docx2md.shから呼び出す
# pip install pptx2md

import os
import subprocess

count = 0
for current, subfolders, subfiles in os.walk("inputf"):
    for fileName in subfiles:
        base, ext = os.path.splitext(fileName)
        if ext == '.pptx' or ext == '.PPTX':
            fullPath = current + "/" + fileName
            print(fullPath)
            count = count + 1
            result = subprocess.run(['pptx2md', fullPath ,'-o' , 'outputf/' + current + '/pptx' + base + '.md' ])
            print(result)

        else:
            print("無視しました。" + fileName )
