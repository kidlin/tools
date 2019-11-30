# made by Tianpei Lin in 2019-11-30

import os
import sys, getopt
import re

def add(argv):
    fileDir=""
    pat=""
    addInfo=""

    if len(argv)==0:
        print("usage: addTopName.py -t <target_dir> -m <match_mode> -a <addInfo>")
        sys.exit()

    try:
        opts, args = getopt.getopt(argv,"ht:m:a:")
    except getopt.GetoptError:
        print("addTopName.py -t <target_dir> -m <match_mode> -a <addInfo>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("usage: addTopName.py -t <target_dir> -m <match_mode> -a <addInfo>")
            sys.exit()
        if opt == "-t":
            fileDir=arg
            if fileDir[-1]!="/":
                fileDir=fileDir+"/"
        elif opt == "-m":
            pat=arg
        elif opt == "-a":
            addInfo=arg
    
    all = os.listdir(fileDir)
    for f in all:
        if re.match(pat,f):
            os.rename(fileDir+f,fileDir+addInfo+f)



if __name__== "__main__":
    add(sys.argv[1:])
