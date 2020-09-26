#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:18:52 2020

@author: darbari
"""
import cv2
import os


video_ext = ['mp4', 'mov', 'avi', 'mkv']
def read_vid(vid):
    cap = cv2.VideoCapture(vid)
    while cap.isOpened():
        ret , frame = cap.read() 
        if (ret == True) :
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        else:
            input('Hit Enter to Exit')
            
            break
    cap.release()
    cv2.destroyAllWindows()   
def vid_write(vid):
    Head, file = os.path.split(vid)
    root, ext = os.path.splitext(vid)
    ext = ext.lower()
    cap = cv2.VideoCapture(vid)
    fps = cap.get(5)
    fwidth = int(cap.get(3))
    fheight = int(cap.get(4))
    OUTPUT_PREFIX = os.path.join(Head, 'output_file'+ext)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    output = cv2.VideoWriter(OUTPUT_PREFIX, fourcc, fps, (fwidth, fheight))   
    while cap.isOpened():
        ret, frame = cap.read() 
        if ret==True:
            img=cv2.flip(frame, 0)
            output.write(img)
            cv2.imshow('frame', img)
            if cv2.waitKey(27) & 0xFF == ord('q'):
                break
        else :
            #input('Hit Enter to Exit')
            
            break
    cap.release()
    output.release()
    cv2.destroyAllWindows()   
if __name__ == '__main__':
    #read_vid() 
    vid = "/home/darbari/test_vid.mp4"
    vid_write(vid)