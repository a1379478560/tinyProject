# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from test import *
#
#
# class MyWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(MyWindow, self).__init__(parent)
#         self.setupUi(self)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     myWin = MyWindow()
#     myWin.show()
#     myWin.pushButton.clicked(
#
#     )
#     sys.exit(app.exec_())


s=input()
l=len(s)
for i in range(l):
    ss=s+s[:i][::-1]
    if ss==ss[::-1]:
        print(len(ss))
        break