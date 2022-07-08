import pyautogui
import time

# time to change tabs from editor to paint;
time.sleep(10)

# it will remain clicked till program ends;
pyautogui.click()

# can be varied according to convininence
distance = 300

while distance > 0:
    
    pyautogui.dragRel(-distance, 0, duration = 0.1)
    
    
    distance -= 10

    #up
    pyautogui.dragRel(0, -distance, duration = 0.1)

    

    pyautogui.dragRel(distance, 0, duration = 0.1)
    

    distance -= 0
    
    #down
    pyautogui.dragRel(0, distance, duration = 0.1)

    
    

