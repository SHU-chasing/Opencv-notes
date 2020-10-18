#-*- coding = utf-8 -*-
#@Time : 2020-10-17 18:38
#@Author : chasing
#@Email : 643601464@qq.com
#@File : test01.py
#@Software: PyCharm
# from PIL import Image
import numpy as np
import cv2
#首先读入一幅图像

def main():

    # img = cv2.imread(r'1.jpg', cv2.IMREAD_UNCHANGED)  # 读入完整图片，包括alpha通道
    # cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)  # 窗口大小自动调整为图像大小
    # cv2.imshow('草地', img)  #第一个为窗口显示的文字
    # cv2.waitKey(0)  #等待窗口关闭
    # cv2.destroyAllWindows()  #习惯

    img = cv2.imread("1.jpg")

    imgGrey = cv2.imread("1.jpg", 0) # 生成灰色图片

    cv2.imshow("img", img)# 展示原图

    cv2.imshow("imgGrey", imgGrey)# 展示灰色图片

    cv2.waitKey()   # 等待图片的关闭

    cv2.imwrite("Copy.jpg", imgGrey) # 保存灰色图片
    cv2.imwrite("./5.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
    cv2.imwrite("./100.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    cv2.imwrite("./0.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    cv2.imwrite("./9.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

    cv2.destroyAllWindows()

if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()