import cv2
from sys import argv
import os.path
from os import path 

# Function to extract frames 
def FrameCapture(pathtovid, pathtoframe): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(pathtovid) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    # Check whether user-supplied directory exists
    if not os.path.exists(pathtoframe):
        os.mkdir(pathtoframe)

    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  

        # Saves the frames with frame-count 
        cv2.imwrite("%sframe%d.jpg" % (pathtoframe, count), image) 
  
        count += 1

if __name__ == '__main__':

    pathtovid = argv[1]
    pathtoframe = argv[2]
    FrameCapture(pathtovid, pathtoframe)