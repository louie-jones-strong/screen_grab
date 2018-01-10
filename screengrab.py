import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record(): 
    while(True):
        last_time = time.time()
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        time_taken = time.time()-last_time



        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        cv2.waitKey(1)
        time_taken = time.time()-last_time
        print("FPS: " + str(1/time_taken))

screen_record()