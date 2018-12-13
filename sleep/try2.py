import numpy as np 
import cv2
img=cv2.imread('C:/Users/ASUS/Pictures/bilibili/p.png',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("Image")
#cv2.imshow('Image',img)#图片的输出
res1= cv2.resize(img,(1000,500))   #对图片进行缩放，第一个参数是读入的图片，第二个是制定的缩放大小
cv2.imshow('Image',res1)
cv2.waitKey (0)
cv2.destroyAllWindows()  