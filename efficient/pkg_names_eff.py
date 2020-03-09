#!/home/william/anaconda3/bin/python


import re


pth = '/home/william/Desktop/'

with open(pth + 'packsone.txt', 'r+') as f:
    pn = f.readlines()

#
l = [mo.group() for pn in pn for mo in [re.search(r"((?:\w+-)+\w+)| (\w+)", pn)] if mo]

with open(pth + 'packsnew_test.txt', 'w+') as f:
    [f.write(str(item).replace("'", "") + "\n") for item in l]
