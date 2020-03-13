
#!/home/william/anaconda3/bin/python


import re


pth = '/home/william/Desktop/'

with open(pth + 'packages_orig.txt', 'r+') as file:
     lib = file.readlines()

packages = [mo.group() for lib in lib for mo in [re.search(r"((?:\w+-)+\w+)| (\w+)", lib)] if mo]

with open(pth + 'packages_new.txt', 'w+') as file:
    [file.write(str(item).replace("'", "") + "\n") for item in packages]