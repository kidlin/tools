# made by Tianpei Lin in 2019-11-30

import os
import sys, getopt
import re

def add(argv):
    fileDir=""
    pat=""
    replaceInfo=""

    if len(argv)==0:
        print("usage: replacePartName.py -t <target_dir> -m <match_mode> -a <replaceInfo>")
        sys.exit()

    try:
        opts, args = getopt.getopt(argv,"ht:m:a:")
    except getopt.GetoptError:
        print("replacePartName.py -t <target_dir> -m <match_mode> -a <replaceInfo>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("usage: replacePartName.py -t <target_dir> -m <match_mode> -a <replaceInfo>")
            sys.exit()
        if opt == "-t":
            fileDir=arg
            if fileDir[-1]!="/":
                fileDir=fileDir+"/"
        elif opt == "-m":
            pat=arg
        elif opt == "-a":
            replaceInfo=arg
    
    all = os.listdir(fileDir)
    for f in all:
        newName=re.sub(pat,replaceInfo,f,1)
        os.rename(fileDir+f,fileDir+newName)



if __name__== "__main__":
    add(sys.argv[1:])
