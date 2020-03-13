#!/home/william/anaconda3/bin/python


import re


'''
==============================================================================
in a nutshell, the following script just takes an existing file that holds a
list of python packages with specific versions, then creates a new file that
holds only the names of the packages without version constraints; there are
much easier methods to do this, especially using conda, but practice using
regular expressions is always needed in my case; please let me know of issues
that are sure to come up often and quickly if anyone actually uses this...
tl; dr. the following is only for those with time to waste on my pointless
blabbering:
the idea of this simple script is to remove any version constraints from an
existing file.  the traditional example could be a requirements.txt file, 
often used to set up the correct virtual environment dependencies for 
installation of a particular package.  while a large list of 
packages might be great to set up a new environment for data science or some
other field, if they are all set to older or outdated package versions, this
could be quite limiting for certain projects.  for this reason, this offers
a quick and easy method to split the list of package names from the versions.
by doing this, and having a file with only the package names, then conda or 
pip (or whatever package installation manager one chooses to use) should
default to automatically installing the most recent version of the package
available. furthermore, if the user wants, it is possible to update the
versions using brute force for relatively short files, or (a much better 
option in my opinion) the user could extend the script to include a web
crawler/scraper that will find the most recent version of the packages, and
update the file to include these versions. although if one is seeking
stability and afraid that once the packages are installed, then while 
working on a project, the package version might get updated and cause issues,
there is a simple method around this; a few examples to help by using 
conda are below. similar methods are available for pip with the use of 
'pipreqs', deatils available at "https://github.com/bndr/pipreqs". 
once the packages are originally installed into a specific environment, the 
user can then export a list of the packages with their respective versions in
a text file using either of the following, depending on personal preference
and/or reproduction needs:
'conda list --explicit > pkgs.txt' 'conda list --export > pkgs.txt'
or to export a yaml file with specifications pertaining to the overall
virtual environment, which can also be used to reproduce the environment:
'conda env export --name base > base_env.yml' 
'conda env export --name base --no-builds > base_env.yml'
with "base" above being the environment name.
the inefficient, looping implementations of these scripts will contain 
overly detailed notation, while the efficient implementations using list
comprehension will not have any comments, since basically the same things
are being done, just in a different way.  
'''

# define the path (here the path is to the desktop but in reality it
# should probably go to the directory of the virtual environment;
# assign to 'pth'
pth = "/home/william/Desktop/"

# open file name 'packages_orig.txt' with ability to read data from it;
# file name is arbitrary but should already exist where defined path leads,
# (the file should contain a list of packages with version contraints; for
# example, one line may read "numpy==1.17")
with open(pth + "packages_orig.txt", "r+") as file:
    #  assign contents of file to variable 'lib'
    lib = file.readlines()

# create new empty list named 'packages'
packages = []

# cycle through each line in 'lib'
for i in range(len(lib)):
    # define regular expression pattern that will leave off the package versions;
    # assign to variable 'pattern'
    pattern = re.compile(r"((?:\w+-)+\w+)| (\w+)")
    # return any item in 'lib' that meets the rules of 'pattern' defined above
    # assign to variable 'match_object' (technically, this should be the type returned)
    match_object = pattern.search(str(lib[i]))
    # append each 'group()' of 'match_object' to list 'packages'
    packages.append(match_object.group())
    # increment counter by one (probably not necessary, but we are being purposefully extra
    # explicit here for learning purposes, in case that was not obvious...)
    i += 1

# create new file named 'packages_new.txt' with ability to write to it;
# (file name is arbitrary)
with open(pth + "packages_new.txt", "w+") as file:
    # cycle through each item in 'packages'
    for item in packages:
        # write each item (package name) to a new line,
        # while removing the quotes around the name
        file.write(str(item).replace("'", "") + "\n")