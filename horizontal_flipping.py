# -*- coding:utf-8 -*-

import cv2
import os
import sys
import re
import xml.etree.ElementTree as ET
from PIL import Image

imgreadpath = 'E:\\Users\\yolov5-develop\\VOCData_EL\\JPEGImages\\'     # 原始jpg存放的文件夹
imgwritepath = 'E:\\Users\\yolov5-develop\\VOCData_EL\\JPEGImages_flip\\'  # 水平翻转后的jpg保存文件夹

xmlreadpath = 'E:\\Users\\yolov5-develop\\VOCData_EL\\Annotations\\'     # 原始xml存放的文件夹
xmlwritepath = 'E:\\Users\\yolov5-develop\\VOCData_EL\\Annotations_flip\\'  # 水平翻转后的xml保存文件夹

# 图像水平翻转
def flitimg(imgname):
    image = cv2.imread(imgname)
    name = imgname.split('\\')[-1].split('.')[-2]
    id = imgname.split('\\')[-1].split('.')[0]
    image_f = cv2.flip(image, 1)  # 1：水平翻转
    cv2.imwrite(imgwritepath + 'f_' + id + '.jpg', image_f)

# xml同步水平翻转
def flitxml(xmlname):
    bwidth = ''
    bheight = ''
    bdepth = ''

    text = open(xmlname).read()
    f_test = open(xmlwritepath + 'f_' + xmlname.split("\\")[-1].split('.')[-2] + '.xml', 'w')

    text = re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", text)
    root = ET.fromstring(text)

    if root.findtext('folder') == ' ':
        print("no folder filename")

    else:
        folder = root.findtext('folder')

    if root.findtext('filename') == ' ':
        print("no filename filename")

    else:
        filename = root.findtext('filename')

    if root.findall('size') == []:
        print("no size filename")

    else:
        size = root.findall('size')
        print(size)
        size = size[0]
        # bwidth = size.findtext('width')
        # bheight = size.findtext('height')
        bdepth = size.findtext('depth')
    img = Image.open(imgwritepath + 'f_' + xmlname.split("\\")[-1].split('.')[-2] + '.jpg')
    bwidth, bheight = img.size
    # bdepth = 3
    # size = root.findall('size')
    # bdepth = size.findtext('depth')

    f_test.write('<annotation>\n')
    f_test.write('	<folder>' + folder + '</folder>\n')
    f_test.write('	<filename>' + filename + '</filename>\n')
    f_test.write('	<size>\n')
    f_test.write('		<width>' + str(bwidth) + '</width>\n')
    f_test.write('		<height>' + str(bheight) + '</height>\n')
    f_test.write('		<depth>' + str(bdepth) + '</depth>\n')
    f_test.write('	</size>\n')

    if root.findall('object') == []:
        print("no object filename:", filename)
    else:
        for object in root.findall('object'):
            label = object.findtext('name')
            x1 = object.findtext('bndbox/xmin')
            y1 = object.findtext('bndbox/ymin')
            x2 = object.findtext('bndbox/xmax')
            y2 = object.findtext('bndbox/ymax')

            f_test.write('	<object>\n')
            f_test.write('		<name>' + label + '</name>\n')
            f_test.write('		<bndbox>\n')
            f_test.write('			<xmin>' + str(int(bwidth) - int(x1) - (int(x2) - int(x1))) + '</xmin>\n')
            f_test.write('			<ymin>' + y1 + '</ymin>\n')
            f_test.write('			<xmax>' + str(int(bwidth) - int(x2) + (int(x2) - int(x1))) + '</xmax>\n')
            f_test.write('			<ymax>' + y2 + '</ymax>\n')
            f_test.write('		</bndbox>\n')
            f_test.write('	</object>\n')

    f_test.write('</annotation>\n')
    f_test.close()

if __name__ == '__main__':

    imgnames = os.listdir(imgreadpath)
    for imgname in imgnames:
        imgname = imgreadpath + imgname
        flitimg(imgname)

    xmlnames = os.listdir(xmlreadpath)
    for xmlname in xmlnames:
        xmlname = xmlreadpath + xmlname
        flitxml(xmlname)
