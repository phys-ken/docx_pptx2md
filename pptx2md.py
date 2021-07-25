# coding:utf-8

import os
import subprocess

# docx2md.shから呼び出す
# pip install pptx2md


count = 0
for current, subfolders, subfiles in os.walk("inputf"):
    for fileName in subfiles:
        base, ext = os.path.splitext(fileName)
        if ext == '.pptx' or ext == '.PPTX':
            fullPath = current + "/" + fileName
            print(fullPath)
            count = count + 1
            result = subprocess.run(['pptx2md', fullPath ,'-o' , 'outputf/' + current + '/pptx' + base + '.md' , '--disable_wmf' ])
            print(result)

        else:
            print("無視しました。" + fileName )
