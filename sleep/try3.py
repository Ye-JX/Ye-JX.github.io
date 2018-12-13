import numpy as np 
import cv2
cap=cv2.VideoCapture('need1.avi')
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
while(cap.isOpened()):
  ret, frame = cap.read()
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  if ret == True
    cv2.imshow('Frame',cv2.resize(gray,(200,300)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else: 
    break
cap.release()
cv2.destroyAllWindows()
