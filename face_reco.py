# -*- coding: utf-8 -*-
__author__ = 'lenovo'

#使用opencv中的haar方法进行静态图片的人脸检测
import cv2
#加载分类器
face_pattern = cv2.CascadeClassifier('C:\Python27\Scripts\opencv\sources\data\haarcascades\haarcascade_frontalface_alt.xml')

sample_image = cv2.imread('3.jpg')#以灰度模式读入图片
color = (255,255,0)#设置人脸框的颜色
size = sample_image.shape[:2]#获得当前桢彩色图像的大小,即图像矩阵的行列
image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)#将图片转换为灰度图片
cv2.equalizeHist(image, image)

divisor = 15
h, w = size
minSize = (int(w/divisor), int(h/divisor))#这里加了一个取整函数
faceRects = face_pattern.detectMultiScale(image, 1.1, 3, cv2.CASCADE_SCALE_IMAGE, minSize)#人脸检测
if len(faceRects) > 0:#如果人脸数组长度大于0
    for faceRect in faceRects: #对每一个人脸画矩形框
            x, y, w, h = faceRect
            cv2.rectangle(sample_image, (x, y), (x+w, y+h), color)

cv2.imwrite('3detect.jpg', sample_image)
cv2.imshow("test", sample_image)#显示图像，test为窗口名，而sample_image为显示图像
cv2.waitKey(0)
cv2.destroyAllWindows()

#显示图片
# image = cv2.imshow('img', image)
# cv2.waitKey(0) #等待接受键盘按键
# cv2.destroyAllWindows() #销毁窗口
