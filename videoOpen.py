#-*- coding = utf-8 -*-
#@Time : 2020-10-19 16:32
#@Author : Jiancong Zhu
#@Email : 643601464@qq.com
#@File : videoOpen.py
#@Software: PyCharm
import cv2
dataFaceUrl = r'E:\opencv\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml'
dataEyesUrl = r'E:\opencv\opencv-master\data\haarcascades\haarcascade_eye.xml'
videoUrl=r'D:\Desktop\python\demo\testOpencv\video1.mp4'
eye_cascade = cv2.CascadeClassifier(dataFaceUrl)
face_cascade = cv2.CascadeClassifier(dataFaceUrl)
def main():
    cap=cv2.VideoCapture(videoUrl)
    while True:
        ret,frame=cap.read()
        # cv2.imshow('video',frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        BBox = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in BBox:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        height, width = frame.shape[:2]
        reSize2 = cv2.resize(frame, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('release', reSize2)
        c = cv2.waitKey(100//30)
        if c==27:#按下esc退出
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
    print("Hello, world!")