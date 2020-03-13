#!/home/william/anaconda3/bin/python


import requests
from bs4 import BeautifulSoup


'''
=============================================================================
quick explanation: the following script pulls all packages associated with 
some specifc anaconda release and operating system, puts them into a list, 
removes all the anaconda specifc packages, and outputs the contents to a file
to use as a 'requirements.txt' file after creating a python virtual 
environment. the script below is for python version 3.7 running on a 
linux 64-bit os; this can be changed by choosing a different combination from
"https://docs.anaconda.com/anaconda/packages/", which is the website that
provides the table from which we are pulling (or "scraping") the data.
=============================================================================
'''


# define website address ("url"); assign to variable 'url'
url = 'https://docs.anaconda.com/anaconda/packages/py3.7_linux-64/'

# use 'requests' package to get webpage from the server; assign to 'req'
req = requests.get(url)

# confirm we have the page by viewing following output,
# which, if successful, should be '<Response [200]>'
print(req)

# create object by passing the constructor the html content
# and specifying the type of parser to use; assign to 'soup'
soup = BeautifulSoup(req.content, 'html.parser')

# select all 'tr' tags of the 'table',
# this will return each row from the table, including headers;
# assign to variable 'trs'
trs = soup.select('table tr')

# change each row within 'trs' to a list
for i in range(len(trs)):
    trs[i] = list(trs[i])


### now we have a multi-dimensional array containing,
### where the first index is the row number, and
### the second index is either a '\n' newline character
### or an element from the row
### (for example, 'trs[1][3]' could return '<td>0.1.0</td>', the version)


# create a new empty list; assign to 'l'
liblist = []

# cycle through each element in 'trs', and if the
# data meets our criteria (no mention of "anaconda" or "Name",
# and the second index is equivalent to 1),
# then we append the data to the empty list 'l'
for i in range(len(trs)):
    if "conda" not in str(trs[i]).lower() \
            and "name" not in str(trs[i]).lower():
        for j in range(len(trs[i])):
            if j == 1:
                liblist.append(trs[i][j])

# create empty list to append packages; assign to 'packages'
packages = []

# cycle through 'l' and filter out each package name,
# using '.text.strip()', as long as it does not begin with '_'
# (anaconda specifc packages will start with an underscore),
# then append the package name to the 'packages' list
for i in range(len(liblist)):
    n = liblist[i].text.strip()
    if not str(n).startswith('_'):
        packages.append(n)


### now all the package names should be in the 'packages' list
### however, we still need to output the contents to a text file
### named 'requirements.txt' and remove the quotations around the names
### so the 'requirements.txt' file can be read properly;


# define the path (here the path is to the desktop but in reality it
# should probably go to the directory of the virtual environment;
# assign to 'pth'
pth = '/home/william/Desktop/'

# create file name 'requirements.txt'; of course, the name of the
# file is arbitrary as long as we remember to use the corret name when
# calling 'python3 -m pip install -r <requirements.txt>' (although if
# the project will be pushed to github, it is probably best to stick
# with the traditional standard, especially since others might have
# personal scripts that use the name 'requirements.txt');
# we also cycle through packages and write each package name to a new
# line, while removing the quotes around the name;
with open(pth + 'requirements.txt', 'w+') as file:
    for item in packages:
        file.write(str(item).replace("'", "") + "\n")
