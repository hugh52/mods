#!/home/william/anaconda3/bin/python


import re


'''
==============================================================================
the following script just takes an existing file that holds a list of python
packages with specific versions, then creates a new file that holds only the 
names of the packages without version constraints.
==============================================================================
'''

# define the path (here the path is to the desktop but in reality it
# should probably go to the directory of the virtual environment, or really
# wherever the user has saved the file containing packages and versions);
# assign to 'pth'
pth = "/home/william/Desktop/"

# open file name 'packages_orig.txt' with ability to read data from it;
# file name is arbitrary but should already exist where defined path leads,
# (the file should contain a list of packages with version constraints; for
# example, one line may read "numpy==1.17")
with open(pth + "packages_orig.txt", "r+") as file:
    #  assign contents of file to variable 'lib'
    lib = file.readlines()

# create new empty list named 'packages'
packages = []

# cycle through each line in 'lib'
for i in range(len(lib)):
    # define regular expression pattern that will leave off package versions;
    # assign to variable 'pattern'
    pattern = re.compile(r".*?(?=(?:=))")
    # return any item in 'lib' that meets the rules of 'pattern' defined above
    # assign to variable 'match_object'
    # (technically, this should be the type returned)
    match_object = pattern.search(str(lib[i]))
    # append each 'group()' of 'match_object' to list 'packages'
    packages.append(match_object.group())
    # increment counter by one (probably not necessary, but we are being
    # purposefully extra explicit here for learning purposes, in case that
    # was not obvious...)
    i += 1

# create new file named 'packages_new.txt' with ability to write to it;
# (file name is arbitrary)
with open(pth + "packages_new.txt", "w+") as file:
    # cycle through each item in 'packages'
    for item in packages:
        # write each item (package name) to a new line,
        # while removing the quotes around the name
        file.write(str(item).replace("'", "") + "\n")
