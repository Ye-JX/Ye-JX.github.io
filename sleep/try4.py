import os
import cv2
import numpy as np 

KeyFrame=26
counter=1
pre_frame = None

cap=cv2.VideoCapture('need2.avi') 
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('size:'+repr(size))
if(cap.isOpened()==False):
    print("False!!!")
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret:
        if counter % KeyFrame == 1:
            
            #gray=cv2.resize(frame,(300,200))  
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame',gray)
            if cv2.waitKey(25)&0xFF==ord('q'):
              break
#视频的输入，长宽转换，灰度转换  
            
            cv2.imshow('lwpCVWindow',cv2.resize(gray,(200,300)))
            gray=cv2.GaussianBlur(gray,(21,21),0)
            if pre_frame is None:
                pre_frame=gray
                print("wertyugdfghjkdfcgvbhnj")
            else:
                img=cv2.absdiff(pre_frame,gray)#差分图
                thresh=cv2.threshold(img,100,255,cv2.THRESH_BINARY)[1]#将灰度图二值化
                thresh=cv2.dilate(thresh,None,iterations=2)#膨胀
                image,contours,hierarchy=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#提取图像轮廓
                cv2.imshow('frame12',thresh)
                for x in contours:
                    if cv2.contourArea(x)<1000:
                        continue
                    else:
                        cv2.imwrite('image.jpg',frame)
                        cv2.imshow('frame',frame)
                        break
                pre_frame=gray
            counter+=1
            if cv2.waitKey(0)&0xFF==ord('q'):
                break
        else:
            break

cap.release()
cv2.destroyAllWindows()
