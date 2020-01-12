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

def projectDepth(folder1, folder2, width, height, K1_, K2_, R_, t_):   
    all = os.listdir(folder1)
    all.sort()
    length=len(all)
    if length==0:
        return
  
    K1=np.loadtxt(K1_, delimiter=' ')
    K2=np.loadtxt(K2_, delimiter=' ')
    R=np.loadtxt(R_, delimiter=' ')
    t=np.loadtxt(t_, delimiter=' ')
    t=1000*np.mat(t).transpose()
    print("K of the first cam:")
    print(K1)
    print("K of the second cam:")
    print(K2)
    print("Rotation:")
    print(R)
    print("Translation:")
    print(t) 

    rows=int(height)
    cols=int(width)
    
    num=0
    while 1:
        depth=cv.imread(folder1+'/'+all[num],-1)
        sp=depth.shape
        new_depth=np.zeros((rows,cols), dtype=np.uint16)
        for i in range(sp[0]):
            for j in range(sp[1]):
                d=float(depth[i][j])
                if d>0:
                    p1=d*np.linalg.inv(K1)*np.mat([j,i,1]).transpose()
                    p2=R*p1+t
                    pixel=K2*p2
                    d_cur=float(pixel[2])
                    if d_cur>0:
                        u=int(pixel[0]/d_cur)
                        v=int(pixel[1]/d_cur)
                        if u>=0 and u<cols-1 and v>=0 and v<rows-1:
                            new_depth[v][u]=d_cur
                            new_depth[v][u+1]=d_cur
                            new_depth[v+1][u]=d_cur
                            new_depth[v+1][u+1]=d_cur       
        cv.imwrite(folder2+'/'+all[num],new_depth)
        print("transformed %s to %s!" % (folder1+'/'+all[num], folder2+'/'+all[num]))
        
        num=num+1
        if num>=length:
           break
              

if __name__ == '__main__':
    
    # parse command line
    parser = argparse.ArgumentParser(description='''
    This script project depth maps with a format of CV_16U to another one. You need to input K1, K2, R, t (meter). 
    ''')
    parser.add_argument('depth_folder', help='folder')
    parser.add_argument('new_depth_folder', help='folder')
    parser.add_argument('width', help='width of the new image')
    parser.add_argument('height', help='height of the new image')
    parser.add_argument('K1', help='Intrinsic Matrix for the first range sensor')
    parser.add_argument('K2', help='Intrinsic Matrix for the second camera')
    parser.add_argument('R', help='Rotation Matrix from cam1 to cam2 (3x3)')
    parser.add_argument('t', help='Translation Matrix from cam1 to cam2 (3x1)')
    args = parser.parse_args()

    projectDepth(args.depth_folder, args.new_depth_folder, args.width, args.height, args.K1, args.K2, args.R, args.t)
            
