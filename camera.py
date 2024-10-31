import cv2
from pprint import pprint
import sys
import numpy

cap = cv2.VideoCapture(0)

while True:
    #frame - сам кадр
    ret, frame = cap.read()
    print(ret)
    for el in frame:
        for i in el:
            print(i, end = '')
    pprint((frame))
    #название окна, сам кадр
    cv2.imshow('camera', frame)
    #Ожидать нажатия клавишь 1 мс
    cv2.waitKey(1)
    break