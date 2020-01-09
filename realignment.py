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
import sys
import os
import shutil

def copy2newFolder(associate, folder1, folder2, skip_first, skip_second):
    f = open(associate,'r')
    data = f.readlines()
    f.close()
    
    name1=[]
    name2=[]
    for line in data:
        list = line.strip('\n').split(' ')
        name1.append(list[1])
        name2.append(list[3])
        

    if not skip_first:
        if not os.path.exists('image_0'):
            os.makedirs('image_0')
        if folder1[-1] != '/':
            folder1=folder1+'/'
        for i in name1:
            shutil.copyfile(folder1+i,'image_0/'+i)
            print("copy %s to %s!" % (folder1+i, 'image_0/'+i))
        
    if not skip_second:
        if not os.path.exists('image_1'):
            os.makedirs('image_1')
        if folder2[-1] != '/':
            folder2=folder2+'/'
        for i in name2:
            shutil.copyfile(folder2+i,'image_1/'+i)
            print("copy %s to %s!" % (folder2+i, 'image_1/'+i))
        

if __name__ == '__main__':
    
    # parse command line
    parser = argparse.ArgumentParser(description='''
    This script realigns two sequences of images according to the associate file.   
    ''')
    parser.add_argument('first_file', help='associate file')
    parser.add_argument('first_folder', help='folder 1')
    parser.add_argument('second_folder', help='folder 2')
    parser.add_argument('--skip_first', help='do not output associated images from first file', action='store_true')
    parser.add_argument('--skip_second', help='do not output associated images from second file', action='store_true')
    args = parser.parse_args()

    copy2newFolder(args.first_file, args.first_folder, args.second_folder, args.skip_first, args.skip_second)
            
