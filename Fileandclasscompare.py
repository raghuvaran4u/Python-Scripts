import glob
import os,pdb
from os.path import exists, join
rootdir = "C:\\Dev\\PCS_RPOS_Version_6\\Releases\\06_12_C1\\6.1"
allclasses = "C:\\Users\\rk185244\\Desktop\\attachment1.txt"
File_names = []

def searchEventsInDerivedClass(filepaths):
    for file in filepaths:
        with open(file,"r") as w:
            print file
            for lines in w:
                if 'this->EventManager->RegisterForEventNotification' in lines:
                    print lines[lines.find("("):]
                    event = lines[lines.find("(")+1:lines.find(",")]
                    array_derived_class_events.append(event)
                    
def searchEventsInBaseClass(filepaths):
    for file in filepaths:
        with open(file,"r") as w:
            print file
            for lines in w:
                if 'this->EventManager->RegisterForEventNotification' in lines:
                    print lines[lines.find("("):]
                    event = lines[lines.find("(")+1:lines.find(",")]
                    array_base_class_events.append(event)
        
def findfilesforbaseclass(classname):    
    search_classname = classname+"::"
    print search_classname
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".cpp"):
                fullpath = os.path.join(subdir, file)                            
                with open(fullpath) as w:
                    for t in w:
                        if search_classname in t:                            
                            Baseclass_file_names.append(fullpath)
                            break
                        
def findfilesforderivedclass(classname):    
    search_classname = classname+"::"
    print search_classname
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".cpp"):
                fullpath = os.path.join(subdir, file)                            
                with open(fullpath) as w:
                    for t in w:
                        if search_classname in t:                            
                            Derivedclass_file_names.append(fullpath)
                            break
                            
with open(allclasses,"r") as w:    
    for lines in w:
        print "Start of Iteration"
        array_base_class_events = []
        array_derived_class_events = []
        Baseclass_file_names = []
        Derivedclass_file_names = []
        baseclassname = lines[lines.find("public")+8:-1]
        derivedclassname = lines[7:lines.find(":")]
        findfilesforbaseclass(baseclassname)
        searchEventsInBaseClass(Baseclass_file_names)      
        findfilesforderivedclass(derivedclassname)
        searchEventsInDerivedClass(Derivedclass_file_names)
        print "\n"
        print "Common Events in Base and Derived class are:"
        print list(set(array_base_class_events).intersection(array_derived_class_events))
        print "End of iteration"
        print "\n"

