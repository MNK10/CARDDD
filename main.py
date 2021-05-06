from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
import os
from PIL import Image, ImageFilter
from PyQt5.QtGui import*

app = QApplication([])
w1 = QWidget()
w1.show()
w1.setWindowTitle('Easy Editor')

pic = QLabel('Картинка')

b1 = QPushButton('Папка')
b2 = QPushButton('Влево')
b3 = QPushButton('Вправо')
b4 = QPushButton('Размытие')
b5 = QPushButton('Резкость')
b6 = QPushButton('Ч/Б')
b7 = QPushButton('Супер Эффект')

ql1 = QListWidget()

hg = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
hg.addLayout(v1,20)
hg.addLayout(v2,80)

v1.addWidget(b1)
v1.addWidget(ql1)


h1.addWidget(b2)
h1.addWidget(b3)
h1.addWidget(b4)
h1.addWidget(b5)
h1.addWidget(b6)
h1.addWidget(b7)

v2.addWidget(pic, 90)
v2.addLayout(h1)

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.image = None
        self.save_dir = ""

    def loadImage(self, filename):
        self. filename = filename
        image_path = os.path.join(workdir, filename)
        self. image = Image. open(image_path)

    def showImage(self, path):
        pic.hide()
        pixmapimage = QPixmap(path)
        w, h = pic.width(), pic.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        pic.setPixmap(pixmapimage)
        pic. show()

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_new(self):
        self.image = self.image.filter(ImageFilter.MaxFilter)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def rez(self):
        self.image = self.image.filter(ImageFilter.DETAIL)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path) 

    def zer(self):
        self.image = self.image.filter(ImageFilter.SMOOTH)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)               

    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)


workimage = ImageProcessor()

workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def filter(files, extension):
    filenames = list()
    for i in files:
        for j in extension:            
            if i.endswith(j):
                filenames.append(i)
    return(filenames)

def showFilenamesList():
    dghsrh = ['jpg', 'bmp', 'png']
    chooseWorkdir()
    a = filter(os.listdir(workdir),dghsrh)
    ql1.clear()
    ql1.addItems(a)

def showChosenImage():
    if ql1.currentRow() >= 0:
        filename = ql1.currentItem().text()
        workimage.loadImage(filename)
        image_path = os.path.join(workdir, workimage. filename)
        workimage.showImage(image_path)

ql1.currentRowChanged.connect(showChosenImage)

b1.clicked.connect(showFilenamesList)
b6.clicked.connect(workimage.do_bw)
b2.clicked.connect(workimage.left)
b3.clicked.connect(workimage.right)
b5.clicked.connect(workimage.rez)
b4.clicked.connect(workimage.zer)
b7.clicked.connect(workimage.do_new)

w1.setLayout(hg)
w1.resize(700, 500)
app.exec_()