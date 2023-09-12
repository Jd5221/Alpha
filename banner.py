from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sys
display_monitor = 1
app = QtWidgets.QApplication(sys.argv)
screen = QtWidgets.QDesktopWidget().screenGeometry(display_monitor)
x = int(screen.width())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        MainWindow.setAttribute(Qt.WA_NoChildEventsForParent, True)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        MainWindow.setWindowFlag(Qt.WindowStaysOnTopHint)
        MainWindow.setWindowFlag(QtCore.Qt.Tool)
        MainWindow.setWindowOpacity(0.7)
        MainWindow.setEnabled(True)
        MainWindow.resize(x, 17)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, x, 17))
        self.label.setStyleSheet("background-color: rgb(12, 124, 38);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Network Name</p></body></html>"))

if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    monitor = QDesktopWidget().screenGeometry(display_monitor)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.move(monitor.left(), monitor.top())
    MainWindow.show()
    sys.exit(app.exec_())