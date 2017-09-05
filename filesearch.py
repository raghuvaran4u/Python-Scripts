import glob
import os,pdb
from os.path import exists, join
rootdir = "C:\\Dev\\PCS_RPOS_Version_6\\Releases\\06_12_C1\\6.1\\Installation\\StagePackage\\WIT"
subclassname = ""
subsubclassname = ""
allderivedfiles = ""
my_array = []
my_array1 = []
my_array2 = []

print("h")
for subdir, dirs, files in os.walk(rootdir):
        for file in files:
                fullpath = os.path.join(subdir, file)
                with open(fullpath, encoding="utf8") as w:                       
                                for t in w:                                        
                                        if 'RADKDS.RELAYDEF.XML' in t:
                                                print (fullpath)
                                                print (t)
                                               

##for subdir, dirs, files in os.walk(rootdir):
##        for file in files:
##            fullpath = os.path.join(subdir, file)
##            if file.endswith("*.xml"):
##                    print fullpath
##                with open(fullpath) as w:
##                        print fullpath
##                    for t in w:
##                        if 'RadKDS.relaydef.xml' in t:
##                                print 
##                            subclassname = t[6:t.find(":")-1]
##                            my_array.append(subclassname)
##
####
##for p in my_array:
##    print (p)

##for subdir, dirs, files in os.walk(rootdir):
##        for file in files:
##            fullpath = os.path.join(subdir, file)
##            if file.endswith(".h" or ".cpp"):                
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
##
####for p in my_array1:
####    print p
####    
####for filename1 in my_array1:    
####        for subdir, dirs, files in os.walk(rootdir):
####          for file in files:          
####              fullpath = os.path.join(subdir, file)
####              if (file ==  filename1):
####                  print fullpath
######                  if file.endswith(".cpp"):
####                  print file
####                  with open(fullpath) as w:
####                        for t in w:
####                          if 'RegisterForEventNotification' in t:
####                               print t[t.find("(")+1:]
######                               print t[t.find("(")+1:t.find(",")-1]
######
####print "Derived CLasses 2 Starts \n \n \n "
####
####for filename in my_array2:
######    print filename
####    for subdir, dirs, files in os.walk(rootdir):
####      for file in files:          
####          fullpath = os.path.join(subdir, file)
####          if (file ==  filename):
######                  if file.endswith(".cpp"):
####                      print file
####                      with open(fullpath) as w:
####                        for t in w:
####                          if 'RegisterForEventNotification' in t:
####                              print t[t.find("(")+1:]
######                               print t
######                               print t[t.find("(")+1:t.find(",")-1]
##                              
##
##                            
