import cv2
import numpy as np
import glob
import shutil
import os
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


# get bounding box from images by using OpenCV
def get_imgage_range(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 0], dtype="uint8")
    upper = np.array([255, 50, 255], dtype="uint8")
    img = cv2.inRange(img, lower, upper)
    img = cv2.blur(img, (2, 2))
    ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    img = cv2.bitwise_not(img)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=lambda x: cv2.contourArea(x))
    # get bounding box posotion
    xmin, ymin, xmax, ymax = cv2.boundingRect(contours)
    # get the original width,height of the image
    dimensions = img.shape
    h = img.shape[0]
    w = img.shape[1]

    # to calculate the bndBox info of this image for yolo
    xp = (xmin + (xmax - xmin) / 2) * 1.0 / w
    yp = (ymin + (ymax - ymin) / 2) * 1.0 / h
    wp = (xmax - xmin) * 1.0 / w
    hp = (ymax - ymin) * 1.0 / h
    return xp, yp, wp, hp


# go through the dataset folder, and find out all png file
for dirname, _, filenames in os.walk('fruits'):

    # define the output folder
    out_folder = dirname.replace('fruits','.\\')
    # to check if the output folder exists, or create it
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)

    for img_path in glob.iglob(dirname + '\\*.png'):

        dirnames = dirname.split('\\')
        # length of dirnames
        leng = len(dirnames)

        # define the train, test text file
        out_text = '.\\' + dirnames[1] + '.txt'

        # define the output path of images and bndBox label files
        out_img_path = img_path.replace('fruits', '.\\')
        out_lbl_text = os.path.splitext(out_img_path)[0] + ".txt"
        print('img_path: '+ img_path)
        print(dirnames)
        print('out_img_path:'+out_img_path)
        # define class for images
        label = 0

        if dirnames[leng-1] == 'freshapples':
            label = 0
        elif dirnames[leng-1] == 'freshbanana':
            label = 1
        elif dirnames[leng-1] == 'freshoranges':
            label = 2
        elif dirnames[leng-1] == 'rottenapples':
            label = 3
        elif dirnames[leng-1] == 'rottenbanana':
            label = 4
        elif dirnames[leng-1] == 'rottenoranges':
            label = 5

        # to generate image's yolo lable
        if os.path.exists(img_path):
            # get yolo label
            xmin, ymin, xmax, ymax = get_imgage_range(img_path)
            # to save yolo label
            with open(out_lbl_text, 'w+') as f:
                f.write('%s %s %s %s %s\n' % (label, xmin, ymin, xmax, ymax))
            # add image path to train.txt, text.txt
            with open(dirnames[1] + '.txt', 'a+') as f:
                line_txt = [out_img_path, '\n']
                f.writelines(line_txt)
            # copy image file to output
            shutil.copyfile(img_path, out_img_path)
