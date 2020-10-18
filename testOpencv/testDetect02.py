#-*- coding = utf-8 -*-
#@Time : 2020-10-18 16:32
#@Author : chasing
#@Email : 643601464@qq.com
#@File : testDetect02.py
#@Software: PyCharm

import cv2
dataFaceUrl = r'E:\opencv\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml'
dataEyesUrl = r'E:\opencv\opencv-master\data\haarcascades\haarcascade_eye.xml'
imgUrl = r"D:\Desktop\python\demo\testOpencv\test.jpg"
eye_cascade = cv2.CascadeClassifier(dataFaceUrl)
face_cascade = cv2.CascadeClassifier(dataFaceUrl)
def main():
    #你好，世界！
    print("Hello World!")

    faceDetect(imgUrl)
def eyesDetect(x, y, w, h,img,gray):
    face_gray = gray[y:y + h, x:x + w]
    face_color = img[y:y + h, x:x + w]
    # 眼睛识别
    eyes = eye_cascade.detectMultiScale(face_gray)
    # 绘制出识别到的眼睛
    for (e_x, e_y, e_w, e_h) in eyes:
        cv2.rectangle(face_color, (e_x, e_y), (e_x + e_w, e_y + e_h), (0, 255, 0), 2)  # 绘制眼睛方框
    cv2.destroyAllWindows()

def faceDetect(imgUrl):
    # 加载haar级联分类器
    # 读取进行检测的图像
    img = cv2.imread(imgUrl)
    # 将原图像转为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 使用级联分类器进行人脸检测 返回值为 人脸的bounding box参数（左上角坐标（x,y），矩形框长和宽）
    # 如果有多张人脸 则返回一个四维数组
    BBox = face_cascade.detectMultiScale(gray, 1.3, 5)
    # 绘制矩形框
    for (x, y, w, h) in BBox:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        eyesDetect(x, y, w, h,img, gray)
    # 显示检测结果
    # cv2.namedWindow('FaceDetection')    #原图
    # cv2.imshow('FaceDetection', img)
    # 保存检测结果
    cv2.imwrite('result.jpg', img)
    height, width = img.shape[:2]
    reSize2 = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('release', reSize2)
    cv2.waitKey(0)

if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()