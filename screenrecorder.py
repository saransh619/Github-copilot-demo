# screen recorder in python
import cv2
import numpy as np
import pyautogui
SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, SCREEN_SIZE)
while True:
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    out.write(img)
    cv2.imshow('window', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
cv2.destroyAllWindows()

