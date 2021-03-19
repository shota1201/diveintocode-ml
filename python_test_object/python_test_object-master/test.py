"""
このファイルに解答コードを書いてください
"""
import re

with open('sample1.txt') as f:
    content = f.read()
    content = content.replace("\n", ",").split(",")
content.pop(-1)
    
m = int(content[-1])
content.pop(-1)

def separate(input_content):
    i = re.findall('[0-9]+', input_content)
    s = re.findall('[a-z]+', input_content)
    return i, s

tmp_dict = {}
integer_list = []
for j in range(len(content)):
    i, s = separate(content[j])
    i = i[-1]
    i = int(i)
    s = s[-1]
    tmp_dict[i] = s
    if m % i == 0:
        integer_list.append(i)

integer_list.sort()
output = [tmp_dict[i] for i in integer_list]
print(output)