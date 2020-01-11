#!/usr/bin/python
# Software License Agreement (BSD License)
#
# Copyright (c) 2013, Juergen Sturm, TUM
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of TUM nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Requirements: 
# sudo apt-get install python-argparse


import argparse
import os
import cv2 as cv
import numpy as np

def showDepth(folder):   
    all = os.listdir(folder)
    all.sort()
    length=len(all)
    if length==0:
        return
    
    num=0
    rotate=False
    while 1:
        depth=cv.imread(folder+'/'+all[num],-1)
        if rotate:
            depth=cv.flip(depth,-1)  
        depth=0.03*depth
        img=np.uint8(depth)
        img_color=cv.applyColorMap(img,cv.COLORMAP_JET)
        cv.putText(img_color,all[num],(1,15),cv.FONT_HERSHEY_COMPLEX,0.5,(100,200,200),1)
        cv.imshow('depth',img_color)
        k=cv.waitKey()
        if k==27:
            break
        elif k==97 or k==65:
            num=num-1
        elif k==100 or k==68:
            num=num+1
        elif k==119 or k==87 or k==115 or k==83:
            rotate=bool(1-rotate)
        if num<0:
            num=0
        if num>=length:
           num=length-1
              

if __name__ == '__main__':
    
    # parse command line
    parser = argparse.ArgumentParser(description='''
    This script show depth maps with a format of CV_16U. Press 'A' 'D' to move.  
    ''')
    parser.add_argument('depth_folder', help='folder')
    args = parser.parse_args()

    showDepth(args.depth_folder)
            
