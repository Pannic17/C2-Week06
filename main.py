import math
import os

import cv2

CAT_FACE_HAAR_CASCADE = 'haarcascade_frontalcatface_extended.xml'
CAT_FILENAME = 'cat_test_7.jpg'


def detect(filename):
    # detect the cat face by opencv haarcascade
    # return the coordinates of cat face
    # cv2级联分类器CascadeClassifier,xml文件为训练数据
    face_cascade = cv2.CascadeClassifier(CAT_FACE_HAAR_CASCADE)
    # 读取图片
    img = cv2.imread(filename)
    # 转灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 进行人脸检测
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.02,
                                          minNeighbors=5)
    # 绘制人脸矩形框
    for (x, y, w, h) in faces:
        w_delta = math.ceil(w * 0.1)
        h_delta = math.ceil(h * 0.1)
        print(w, h)
        print(x, y)

        # change the coordinate, increase the rectangle by 10% for each side and move up to include the ears
        x1 = x - w_delta
        y1 = y - h_delta * 2
        x2 = x + w + w_delta
        y2 = y + h

        # draw the cat face, originate and cut
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("### Face Coordinate")
        print(x1, y1, x2, y2)
        print("###################")
        # return x1, y1, x2, y2
        coordinates = [x1, y1, x2, y2]
        positive = True
        for coordinate in coordinates:
            if coordinate < 0:
                positive = False
                break

        # 命名显示窗口
        # cv2.namedWindow('cat')
        # 显示图片
        # cv2.imshow('cat', img)
        # 保存图片
        # cv2.imwrite('cxks.png', img)
        # 设置显示时间,0表示一直显示
        cv2.waitKey(0)
        # return x1, y1, x2, y2
        if w < 30:
            return None
        if positive is True:
            return coordinates
        else:
            return None


def cut(filename):
    # cut the cat face out according to the coordinates given by detection
    # return the image for saving
    coordinates = detect(filename)

    img = cv2.imread(filename)
    if coordinates is not None:
        new = img[coordinates[1]:coordinates[3], coordinates[0]:coordinates[2]]
        # show the cut face
        # cv2.imshow('cut', new)
        cv2.waitKey(0)
        return new
    else:
        return None


def load():
    path = 'datasets/'
    loca = 'datasets/'
    breed = input('Please Enter Breed：')
    count = 0
    # create location
    # os.mkdir((loca+breed))
    file_type = '.jpg'
    path = path + breed + '/original'
    loca = loca + breed + '/faces'
    file_list = os.listdir(path)
    incorrect = 0
    for files in file_list:
        count += 1
        file_path = os.path.join(path, files)
        print(file_path)
        img = cut(file_path)
        if img is not None:
            # original_name = os.path.basename(files)
            new_name = breed + '_' + str(count) + '.jpg'
            print(breed + "-------->No. " + str(count) + " SUCCESS")
            cv2.imwrite(loca + new_name, img)
        else:
            print(files + "-------->No. " + str(count) + " un-usable")
            incorrect += 1
            old = cv2.imread(file_path)
            new_name = breed + '_' + str(count) + '.jpg'
            # cv2.imwrite(loca + new_name, old)
    print("In Total, " + str(incorrect) + "un-usable")
    ###


# cut(filename)
if __name__ == '__main__':
    load() 