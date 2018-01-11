import numpy as np
from PIL import ImageGrab
import cv2 
import time
import keyboard
import random

def screen_record(): 
    time.sleep(5)
    adress = "data_set.txt"
    #file = open(adress,"w")
    #file.close()
    loop = 0
    while(True):
        last_time = time.time()
        img = ImageGrab.grab(bbox=(0,0,1920,1080))
        img =  np.array(img)
        img = cv2.resize( img , (int(1920/3), int(1080/3)) )
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #cal_stuff( img , adress )

        cv2.imshow('window',img)
        cv2.waitKey(1)
        time_taken = time.time()-last_time
        print("FPS: " + str(1/time_taken))
        loop += 1

def cal_stuff( input , adress ):
    output = ["0","0","0","0"]

    if keyboard.is_pressed('w'):
        output[0] = "1"

    if keyboard.is_pressed('a'):
        output[1] = "1"

    if keyboard.is_pressed('s'):
        output[2] = "1"

    if keyboard.is_pressed('d'):
        output[3] = "1"

    print(output)
    file = open(adress,"a")
    #file.write("!" + ",".join(output) + "\n")
    file.write(str(output[2]) + "\n")
    file.close()
    return

def press_keys(inputs):
    print(inputs)

    if inputs[0] == "1":
        keyboard.press("w")
    else:
        keyboard.release("w")

    if inputs[1] == "1":
        keyboard.press("a")
    else:
        keyboard.release("a")

    if inputs[2] == "1":
        keyboard.press("s")
    else:
        keyboard.release("s")

    if inputs[3] == "1":
        keyboard.press("d")
    else:
        keyboard.release("d")

    return

time.sleep(5)
while True:
    inputs = [str(random.randint(0,1)),str(random.randint(0,1)),str(random.randint(0,1)),str(random.randint(0,1))]
    #inputs = ["1"]
    press_keys(inputs)
    time.sleep(0.2)
    if keyboard.is_pressed('esc'):
        input()


#screen_record()