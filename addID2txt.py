# made by Tianpei Lin in 2019-11-30

import os
import sys, getopt
import re

def add(argv):
    file=""
    saveFile=""

    if len(argv)==0:
        print("usage: addID2txt.py -t <target_file.txt> -s <saved_file.txt>")
        sys.exit()

    try:
        opts, args = getopt.getopt(argv,"ht:s:")
    except getopt.GetoptError:
        print("usage: addID2txt.py -t <target_file.txt> -s <saved_file.txt>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("usage: addID2txt.py -t <target_file.txt> -s <saved_file.txt>")
            sys.exit()
        elif opt == "-t":
            file=arg
        elif opt == "-s":
            saveFile=arg
    
    f=open(file,'r')
    times=[]
    a=f.readline()
    while len(a):
        times.append(a)
        a=f.readline()
    f.close()
    print("find %d timestamps!" % len(times))

    f=open(saveFile,'w')
    idx=0
    for t in times:
        f.write(str(idx)+" "+t)
        idx=idx+1
    f.close()
    print("transform %s to %s" %(file, saveFile))




if __name__== "__main__":
    add(sys.argv[1:])
