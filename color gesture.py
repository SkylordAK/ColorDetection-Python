import cv2
import cv2.cv as cv
import numpy as np
import pyautogui
pyautogui.FAILSAFE = False
x = 1366
y = 0
cap = cv2.VideoCapture(0)
cap.set(cv.CV_CAP_PROP_FRAME_WIDTH, 1366)
cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 768)
while 1:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lb = np.array([100,100,120], np.uint8)
    ub = np.array([150,255,255], np.uint8)
    mask = cv2.inRange(hsv,lb,ub)
    main = cv2.bitwise_and(frame,frame, mask= mask)
    pixel = np.where(mask)
    t = (pixel[1])
    u = (pixel[0])
    try:
        x = t[1]
    except:
        np.append([1],[2])
    try:
        y = u[1]
    except:
        np.append([1],[2])
    x = 1366-x
    cv2.circle(frame, (x, y), 8, (0,0,255), 3)
    print x,y
    cv2.imshow('detected',main)
    #Used for moving cursors
    #pyautogui.moveTo(x,y)
    #pyautogui.click(clicks=2,interval=0.25)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
