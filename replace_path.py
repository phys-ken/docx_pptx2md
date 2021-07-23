## 引数をふたつとる
# filename , text

import sys
import re

print (sys.argv[0])
print (sys.argv[1])
print (sys.argv[2])

filename = sys.argv[1]
with open(filename, 'r') as f:
    fileText = f.read()
    tmptext = fileText.replace( sys.argv[2], '')
    finaltext = re.sub('{w(.|\s)*?}', "", tmptext)

with open(filename, 'w') as f:
    f.write(finaltext)