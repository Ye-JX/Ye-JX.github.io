
import os

import random

from _datetime import datetime

 

import cv2

 

path = 'F:\\111'

 

 

# 遍历目录下的视频文件

def get_files(fpath):

    files_list = []

    for i in os.listdir(fpath):

        files_list.append(os.path.join(fpath, i))

    return files_list

 

 

# 视频处理

def process(file, fname):

    # camera = cv2.VideoCapture(0)  # 参数0表示第一个摄像头

    camera = cv2.VideoCapture(file)

    # 参数设置，监测矩形区域

    rectangleX = 880  # 矩形最左点x坐标

    rectangleXCols = 0  # 矩形x轴上的长度

    rectangleY = 650  # 矩形最上点y坐标

    rectangleYCols = 100  # 矩形y轴上的长度

    KeyFrame = 17  # 取关键帧的间隔数，根据视频的帧率设置，我的视频是16FPS

    counter = 1  # 取帧计数器

    pre_frame = None  # 总是取视频流前一帧做为背景相对下一帧进行比较

 

    # 判断视频是否打开

    if not camera.isOpened():

        print('视频文件打开失败！')

 

    width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))

    height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print('视频尺寸（高，宽）:', height, width)

 

    if rectangleXCols == 0:

        rectangleXCols = width - rectangleX

    if rectangleYCols == 0:

        rectangleYCols = height - rectangleY

    start_time = datetime.now()

    print('{} 开始处理文件： {}'.format(start_time.strftime('%H:%M:%S'), fname))

    while True:

        grabbed, frame_lwpCV = camera.read()  # 读取视频流

        if grabbed:

            if counter % KeyFrame == 0:

                # if not grabbed:

                #     print('{} 完成处理文件： {} 。。。  '.format(datetime.now().strftime('%H:%M:%S'),fname))

                #     break

                gray_lwpCV = cv2.cvtColor(frame_lwpCV, cv2.COLOR_BGR2GRAY)  # 转灰度图

                gray_lwpCV = gray_lwpCV[rectangleY:rectangleY + rectangleYCols, rectangleX:rectangleX + rectangleXCols]

                lwpCV_box = cv2.rectangle(frame_lwpCV, (rectangleX, rectangleY),

                                          (rectangleX + rectangleXCols, rectangleY + rectangleYCols), (0, 255, 0),

                                          2)  # 用绿色矩形框显示监测区域

                # cv2.imshow('lwpCVWindow', frame_lwpCV)  # 显示视频播放窗口，开启消耗时间大概是3倍

                gray_lwpCV = cv2.GaussianBlur(gray_lwpCV, (21, 21), 0)

                if pre_frame is None:

                    pre_frame = gray_lwpCV

                else:

                    img_delta = cv2.absdiff(pre_frame, gray_lwpCV)

                    thresh = cv2.threshold(img_delta, 25, 255, cv2.THRESH_BINARY)[1]

                    thresh = cv2.dilate(thresh, None, iterations=2)

                    image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,

                                                                  cv2.CHAIN_APPROX_SIMPLE)

                    for x in contours:

                        if cv2.contourArea(x) < 1000:  # 设置敏感度

                            continue

                        else:

                            cv2.imwrite(

                                'image/' + fname + '_' + datetime.now().strftime('%H%M%S') + '_' + str(

                                    random.randrange(0, 9999)) + '.jpg',

                                frame_lwpCV)

                            # print("监测到移动物体。。。  ", datetime.now().strftime('%H:%M:%S'))

                            break

                    pre_frame = gray_lwpCV

            counter += 1

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):

                break

        else:

            end_time = datetime.now()

            print('{} 完成处理文件： {}  耗时：{}'.format(end_time.strftime('%H:%M:%S'), fname, end_time - start_time))

            break

    camera.release()

    # cv2.destroyAllWindows() #  与上面的imshow对应

 

 

for file in get_files(path):

    fname = file.split('\\')[-1].replace('.mp4', '')

    process(file, fname)
