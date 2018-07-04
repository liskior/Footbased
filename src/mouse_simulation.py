import pyautogui as ptg
import time

# setting fail safes
ptg.FAIL_SAFE = True
ptg.PAUSE = 1
currentMouseX, currentMouseY = ptg.position()
# moving the pointer to screen center
screenWidth, screenHeight = ptg.size()
time.sleep(5)
ptg.click(button='right', x=ptg.position()[0], y=ptg.position()[1])
time.sleep(5)
#while True:
ptg.click(x=ptg.position()[0], y=ptg.position()[1])

time.sleep(5)
    #ptg.click(clicks=2)
    #ptg.scroll(10)
ptg.click(button='middle', x=ptg.position()[0], y=ptg.position()[1])
time.sleep(5)
    #ptg.scroll(-10)
    #ptg.hscroll(10)
    #ptg.hscroll(-10)


