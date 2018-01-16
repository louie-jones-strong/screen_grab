import numpy as np
from screen_grab import grab_screen2 as grab_screen
import cv2 
import os
import time
import keyboard
import random
from play_sound import *

def screen_record(): 
    region = (0,0,1920,1080)
    batch_size = 100
    save_image_on = True
    address = "dataset\\"

    loop = 0
    data_set = []
    while(True):
        last_time = time.time()
        img_og = grab_screen( region=region )


        width = region[2] - region[0] 
        height  = region[3] - region[1] 

        img = cv2.resize( img_og , (int(width/10), int(height/10)) )
        #img = img[  0:58 , 0:192 ]#croped

        data_set += cal_stuff( img )

        if (len(data_set) % batch_size) == 0:
            if save_image_on:
                cv2.imwrite(address + "images\\" + str(loop+1) + ".png" ,img)

            np.save(address + "temps\\"+ "data-set_" + str(loop+1) +".npy", data_set)
            data_set = []
            print("saved!")
            
        time_taken = time.time()-last_time
        print("FPS: " + str(1/time_taken))
        loop += 1
        if keyboard.is_pressed("space"):

            print("stoped!")
            join_files( address , batch_size )
            loop = 0
            data_set = []
            play_sound()
            pause()
    return

def join_files( address , batch_size ):
    if os.path.isfile(address + "total_data-set.npy"):#cheack to see if it is a file already
        total_dataset = [np.load(address + "total_data-set.npy")]
    else: 
        total_dataset = None

    to_loop_to = len(os.listdir(address+"temps\\"))+1
    for loop in range(1,to_loop_to):
        temp_address = address + "temps\\data-set_" + str(loop*batch_size) + ".npy"

        if total_dataset == None:
            total_dataset = [np.load(temp_address)]

        else:
            total_dataset = np.append( total_dataset , [np.load(temp_address)] , axis=1)

        os.remove(temp_address)

    total_dataset = total_dataset[0]

    np.save( address+"total_data-set.npy" , total_dataset )
    print("items in dataset: " + str(len(total_dataset)))
    return

def cal_stuff( img ):
    output = [0,0,0,0]

    if keyboard.is_pressed('w'):
        output[0] = 1

    if keyboard.is_pressed('a'):
        output[1] = 1

    if keyboard.is_pressed('s'):
        output[2] = 1

    if keyboard.is_pressed('d'):
        output[3] = 1

    data_set = [img,output]
    return [data_set]

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

def pause():
    time.sleep(2)
    print("press space button to start: ")
    while keyboard.is_pressed("space") == False :
        time.sleep(0.01)

    for loop in range(3):
        print(str(loop+1))
        time.sleep(1)

    print("started")
    play_sound()

    return

sound_setup("sounds\\ring.ogg")
pause()
screen_record()

