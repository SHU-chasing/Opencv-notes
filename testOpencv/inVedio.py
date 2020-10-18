#-*- coding = utf-8 -*-
#@Time : 2020-10-18 17:12
#@Author : chasing
#@Email : 643601464@qq.com
#@File : inVedio.py
#@Software: PyCharm


def main():
    #你好，世界！
    print("Helloworld!")
    import cv2

    cap = cv2.VideoCapture('沙话(阿悄).mkv')  # 创建一个视频获取对象
    flag = 2000
    cascPath = r'E:\anaconda\python3.7\Lib\site-packages\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml'

    faceCascade = cv2.CascadeClassifier(cascPath)
    faceCascade.load(cascPath)  # 结果为 True

    # 保存视频
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 保存视频的编码
    fps = cap.get(cv2.CAP_PROP_FPS)  # 设置帧频率
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), \
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # 保存视频格式
    out = cv2.VideoWriter('.\沙话1.mp4', fourcc, fps, size)

    while (cap.isOpened()):
        # cap.set(cv2.CAP_PROP_POS_MSEC,flag)# 设置时间标记
        # cap.set(cv2.CAP_PROP_POS_FRAMES,flag) # 设置帧数标记
        try:
            ret, frame = cap.read()  # 获取图像
            # cv2.imshow('%d'%flag, frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        except:
            print('视频已结束')
            break
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        # 画矩形框
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 显示视频
        cv2.imshow('Video', frame)

        # 写入一帧
        out.write(frame)
        cv2.waitKey(10)

        # 键盘 q 键可以提前终止视频
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()