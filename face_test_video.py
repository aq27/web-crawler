# -*- coding: utf-8 -*-
__author__ = 'lenovo'

#使用opencv中的haar方法进行摄像头人脸检测，缺陷：照片上的人像也会识别
import cv2

#加载分类器
face_pattern = cv2.CascadeClassifier('C:\Python27\Scripts\opencv\sources\data\haarcascades\haarcascade_frontalface_alt.xml')

cv2.namedWindow("test")#命名一个窗口
cap = cv2.VideoCapture(0)#笔记本使用内置摄像头，0号摄像头；外置摄像头使用1
success, frame = cap.read()#读取一桢图像，前一个返回值是是否成功，后一个返回值是图像本身
color = (255, 255, 0)#设置人脸框的颜色

while success:
    success, frame = cap.read()
    size = frame.shape[:2]#获得当前桢彩色图像的大小,即图像矩阵的行列
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#将图片转换为灰度图片
    cv2.equalizeHist(image, image) #直方图均衡化，使得灰度范围变大、对比度变大，增强图像

    divisor = 9
    h, w = size
    minSize = (int(w/divisor), int(h/divisor))#这里加了一个取整函数

    #人脸检测，image为检测的灰度图像，1.1表示窗口的递增系数（以10%递增），3为minNeighbors即指定每个候选矩阵应该保留的邻居个数，cv2.CASCADE_SCALE_IMAGE表示按正常比例检测，minSize表示矩形最小的尺寸
    faceRects = face_pattern.detectMultiScale(image, 1.1, 3, cv2.CASCADE_SCALE_IMAGE, minSize)

    if len(faceRects) > 0:#如果人脸数组长度大于0
        for faceRect in faceRects:#对每一个人脸画矩形框
                x, y, w, h = faceRect#x,y分别表示矩形框的坐标，w、h表示矩形框的宽高
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 1)#(x, y)表示矩形框的左上点坐标，(x+w, y+h)表示矩形框的右下点坐标，color表示矩形框的颜色，1表示矩形框的宽度

    cv2.imshow("test", frame)#显示图像，test为窗口名，而sample_image为显示图像
    # cv2.imwrite('detect.jpg', frame)
    key = cv2.waitKey(10)
    c = chr(key & 255)
    if c in ['q', 'Q', chr(27)]:
        break

cv2.destroyAllWindows()

#显示图片
# image = cv2.imshow('img', image)
# cv2.waitKey(0) #等待接受键盘按键
# cv2.destroyAllWindows() #销毁窗口

