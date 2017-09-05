import glob
import os,pdb
from os.path import exists, join
rootdir = "C:\\Dev\\PCS_RPOS_Version_6\\Releases\\06_12_C1\\6.1"
subclassname = ""
subsubclassname = ""
allderivedfiles = ""
my_array = []
my_array1 = []
my_array2 = []

for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            fullpath = os.path.join(subdir, file)
            if file.endswith(".cpp"):                
                with open(fullpath) as w:
                    for t in w:
                        if 'Reboot,' in t:
                                print file
                                print t
##                                subclassname = t[6:t.find(":")-1]
##                                my_array.append(subclassname)
##
##for subdir, dirs, files in os.walk(rootdir):
##        for file in files:
##            fullpath = os.path.join(subdir, file)
##            if file.endswith(".h"):                
##                with open(fullpath) as w:
##                    for t in w:
##                        for p in my_array:
##                            if ': public ' + p in t:
####                                subsubclassname = t[6:t.find(":")-1]
##                                allderivedfiles = t
##                                print allderivedfiles
##                                derivedfilename = allderivedfiles[7:allderivedfiles.find(":")-1] + ".cpp"
####                                basefilename = allderivedfiles[49:allderivedfiles.find(",")-1] + ".cpp"
##                                basefilename = allderivedfiles[allderivedfiles.find("public")+8:-1] + ".cpp"
##                                my_array1.append(derivedfilename)
##                                my_array2.append(basefilename)
