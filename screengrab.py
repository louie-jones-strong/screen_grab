import numpy as np
from PIL import ImageGrab
import cv2 
import time
import keyboard
import random

def screen_record(): 
    adress = "dataset\\"
    file = open(adress + "data-set.txt","w")
    file.close()
    loop = 0
    while(True):
        last_time = time.time()
        img = ImageGrab.grab()
        img =  np.array(img)
        #img = cv2.resize( img , (int(1920/3), int(1080/3)) )
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        cal_stuff( img , adress , loop )

        cv2.imshow('window',img)
        cv2.waitKey(1)
        time_taken = time.time()-last_time
        print("FPS: " + str(1/time_taken))
        loop += 1


def cal_stuff( img , adress , image_number ):
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
    output = ",".join(output)
    save( adress , img , output , image_number )
    return

def save( adress , input_image , output , image_number ):
    image_path = "images//" + str(image_number) + ".png"
    file = open(adress + "data-set.txt","a")
    file.write(image_path + "!" + str(output) + "\n")
    file.close()

    cv2.imwrite(adress + image_path,input_image)

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

input()
time.sleep(5)

screen_record()


while True:
    inputs = ["1",str(random.randint(0,1)),"0",str(random.randint(0,1))]
    #inputs = ["1"]
    press_keys(inputs)
    time.sleep(0.2)
    if keyboard.is_pressed('esc'):
        input()
