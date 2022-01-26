import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
start = time.perf_counter()
time.sleep(2)
end = time.perf_counter()
print("计算米粒个数花费的时间是：",end-start)
img = cv2.imread("image/rice.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,101, 1)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3, 3))
dst=cv2.morphologyEx(dst,cv2.MORPH_OPEN,element)
contours, hierarchy = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(dst,contours,-1,(120,0,0),2)
count=0
for cont in contours:
    count += 1
    rect = cv2.boundingRect(cont)
    cv2.rectangle(img,rect,(0,0,255),1)
    y = 10 if rect[1] < 10 else rect[1]
    cv2.putText(img,str(count), (rect[0],y), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 255, 0), 1)
print('米粒的个数是：',count)
cv2.namedWindow("1", 2)
cv2.imshow('1', img)
cv2.imwrite('image/2333.png',img)
cv2.waitKey()

