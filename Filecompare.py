import glob
import os,pdb
from os.path import exists, join
rootdir = "C:\\Dev\\PCS_RPOS_Version_6\\Releases\\06_12_C1\\6.1"
allclasses = "C:\\Users\\rk185244\\Desktop\\attachment1.txt"
filelocation = ""


def searchbaseclassfile(filename):
    with open(filename,"r") as w:
        for lines in w:
            if 'this->EventManager->RegisterForEventNotification' in lines:
                print lines[lines.find("("):]
                event = lines[lines.find("(")+1:lines.find(",")]
                array_base_class_events.append(event)
                
def searchderivedclassfile(filename):
    with open(filename,"r") as w:
        for lines in w:
            if 'this->EventManager->RegisterForEventNotification' in lines:
                print lines[lines.find("("):]
                event = lines[lines.find("(")+1:lines.find(",")-1]
                array_derived_class_events.append(event)
                
def findbaseclassfile(filename):
    print filename
    for subdir, dirs, files in os.walk(rootdir):
          for file in files:          
              fullpath = os.path.join(subdir, file)            
              if file.endswith(".cpp"):
                  if (file ==  filename):                      
                      print fullpath
                      searchbaseclassfile(fullpath)
def findderivedclassfile(filename):
    print filename
    for subdir, dirs, files in os.walk(rootdir):
          for file in files:          
              fullpath = os.path.join(subdir, file)
              if file.endswith(".cpp"):
                  if (file ==  filename):                      
                      print fullpath
                      searchderivedclassfile(fullpath)                      


with open(allclasses,"r") as w:
    for lines in w:
        array_base_class_events = []
        array_derived_class_events = []
        print "Start of Iteration"
        print "\n"
        print "Base class Name and their Events:"
        baseclassname = lines[lines.find("public")+8:-1] + ".cpp" 
        findbaseclassfile(baseclassname)   
##        for p in array_base_class_events:
##            print p
        print "\n"
        print "Derived class Name and their Events"
##        if (lines[lines.find(":")-1] == " "):
##            derivedclassname = lines[7:lines.find(":")-2] + ".cpp"
##        else:
        derivedclassname = lines[7:lines.find(":")] + ".cpp"
        findderivedclassfile(derivedclassname)         
##        for p in array_derived_class_events:
##            print p
        print "\n"
        print "Common Events in Base and Derived class are:"
        print list(set(array_base_class_events).intersection(array_derived_class_events)) 
        print "End of iteration"
        print "\n"
