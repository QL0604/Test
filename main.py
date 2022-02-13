#!/usr/bin/python
# -*- coding: UTF-8 -*-

#所需要的库
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


#显示图像函数
def cv_show(name,img):
    cv.imshow(name,img)
    cv.waitKey(0)
    cv.destroyAllWindows()

#读取图片cv2.imread("图片路径")
img = cv.imread('./data/1.PNG')
x, y = img.shape[:2]
img1 = img[50:x-50,50:y-50]  #需要保留的区域--裁剪
#参数1 是高度的范围，参数2是宽度的范围

cv.imwrite("1-bak.PNG",img1)
cv.waitKey(0)

#各个边界需要填充的值
top_size,bottom_size,left_size,right_size=(50,50,50,50)
#复制法
replicate=cv.copyMakeBorder(img1,top_size,bottom_size,left_size,right_size,borderType=cv.BORDER_REPLICATE)
#常量法，常数值填充
constant=cv.copyMakeBorder(img1,top_size,bottom_size,left_size,right_size,cv.BORDER_CONSTANT,value=(0,255,0))

cv.imwrite("1-constant-bak.PNG",constant)
cv.imwrite("1-replicate-bak.PNG",replicate)
# img2=img1.copy()
# #在各个图像上添加相应的文本
# cv.putText(img2,"original",(0,50),cv.FONT_HERSHEY_COMPLEX,2,(0,250,0),4,8)
# cv.putText(constant,"",(0,50),cv.FONT_HERSHEY_COMPLEX,2,(0,250,0),4,8)
#
# #显示图像
# cv_show("original",img2)
# cv_show("constant",constant)