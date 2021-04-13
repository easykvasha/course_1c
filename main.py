import re
import numpy as num
import pandas as pan

def parsing(p):
    l = []
    word = p.split(')')
    l.append(int(word[0][1:]))
    if (len(p.split('[')) == 1):
        l.append([None])
    else:
        l.append([])
        words = p.split('[')
        p = words[-1]
        p = re.sub(']', '', p)
        p = re.sub(',', '', p)
        word = p.split()
        for i in word:
            if (len(i.split('/')) == 1):
                l[1].append([int(i)])
            else:
                l[1].append(list(map(int, i.split('/'))))
    return l

file = pan.read_excel('Курсы v.3.0.xls')
nfile = file.transpose().to_numpy(na_value = 0)

for m in range(len(nfile)):
    for n in range(len(nfile[m])):
        if nfile[m][n] == -1:
            nfile[m][n] = [-1]
            break
        nfile[m][n] = parse(nfile[m][n])



