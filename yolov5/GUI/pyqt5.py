import sys
import cv2 as cv
# import os
# import numpy as np
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap, QColor, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QGraphicsDropShadowEffect

from ui import Ui_MainWindow

from Detection import Detect
from Tools.GUIUtils import autoMeas

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)  # 将界面设置为无框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 将界面属性设置为半透明
        self.shadow = QGraphicsDropShadowEffect()  # 设定一个阴影,半径为10,颜色为#444444,定位为0,0
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor("#444444"))
        self.shadow.setOffset(0, 0)
        self.frame.setGraphicsEffect(self.shadow)  # 为frame设定阴影效果


        self.my_timer = QTimer()  # 创建定时器
        self.btn_status = False

        self.my_timer.timeout.connect(self.my_timer_cb)
        self.imgBtn.clicked.connect(self.select_image)
        self.exitBtn.clicked.connect(self.close)
        self.closeBtn.clicked.connect(self.close)
        self.minimalBtn.clicked.connect(self.showMinimized)
        self.videoBtn.clicked.connect(self.startVideo)
        self.modelsCombo.currentIndexChanged[str].connect(self.changeModels)
        # Load YOLOv5 detector
        self.imgLabel.hide()
        self.resultLabel.hide()
        self.detector = Detect()
        self.imgs = []
        self.cap = 0

    # 鼠标左键按下时获取鼠标坐标,按下右键取消
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
        elif event.button() == Qt.RightButton:
            self.m_flag = False

    # 鼠标在按下左键的情况下移动时,根据坐标移动界面
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    # 鼠标按键释放时,取消移动
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False

    # 下拉菜单更改模型触发事件
    def changeModels(self, context):
        if (context == 'ResnetLarge'):
            self.detector.loadModel()
        elif (context == 'MobileNetV3'):
            self.detector.loadModel(weights='results/MobileNetV3_yolo.pt')
        elif (context == 'ResnetTiny'):
            self.detector.loadModel(weights='results/ResnetTiny_yolo.pt')
        else:
            print('Wrong! not found models')

    # 点击选择图片触发事件
    def select_image(self):
        # Show file dialog to select an image file
        if self.btn_status:
            self.startVideo()
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select image file', '', 'Images (*.png *.xpm *.jpg)')
        if file_path:
            # Detect objects in the image
            results, resStr = self.detector.detect(file_path)
            size = results.shape
            # 将默认的bgr转换为rgb格式
            rgb_img = cv.cvtColor(results, cv.COLOR_BGR2RGB)
            # 将bgr格式转换为qt可以识别的格式
            img_dis = QImage(rgb_img, rgb_img.shape[1], rgb_img.shape[0], rgb_img.shape[1] * 3, QImage.Format_RGB888)
            w, h = autoMeas(800, 550, size[1], size[0])
            self.imgLabel.resize(w, h)
            # 加载图片，并设定图片大小
            img_dis = QPixmap(img_dis).scaled(w, h)
            # 显示图片
            self.imgLabel.show()
            self.imgLabel.setPixmap(img_dis)
            self.resultLabel.show()
            self.resultLabel.setText(resStr)

    # 点击 打开/关闭 摄像头触发事件
    def startVideo(self):
        if self.btn_status:
            print('close camera')
            self.btn_status = False
            self.imgLabel.hide()
        else:
            print('open camera')
            self.btn_status = True
            self.resultLabel.setText('')
            self.resultLabel.hide()
            self.imgLabel.show()

        if self.btn_status:
            self.videoBtn.setText('Stop')
            self.my_timer.start(33)  # 30fps
            self.cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # start camera
        else:
            self.videoBtn.setText('Video')
            self.imgLabel.clear()  # 清楚label内容
            self.my_timer.stop()  # 停止定时器
            self.cap.release()  # 关闭摄像头

    # 定时函数 处理摄像头提取的每一帧在界面上的渲染
    def my_timer_cb(self):
        if self.cap:
            """图像获取"""
            ret, self.img = self.cap.read()
            # show = cv.resize(self.img, (640, 480))
            show = cv.flip(self.img, 1)
            """图像处理"""
            show = self.detector.detect(show, 1)
            """处理结果存储"""
            size = show.shape
            w, h = autoMeas(800, 550, size[1], size[0])
            """结果呈现"""
            show = cv.cvtColor(show, cv.COLOR_BGR2RGB)
            showImage = QImage(show.data, show.shape[1], show.shape[0], show.shape[1] * 3, QImage.Format_RGB888)
            self.imgLabel.resize(w, h)
            # 加载图片，并设定图片大小
            img_dis = QPixmap(showImage).scaled(w, h)
            self.imgLabel.setPixmap(img_dis)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyWindow()
    ui.show()
    sys.exit(app.exec_())
