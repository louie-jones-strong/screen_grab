import time
import screengrab

while True:
    time.sleep(0.5)
    img = screengrab.grab_screen()
    print(img)
    input()