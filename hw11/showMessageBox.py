from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

def showMessageBox(dataModel):
    resultMessage = 'Yolo人數: 11' + '\n'
    resultMessage = resultMessage + 'Google人數: 5' + '\n'
    resultMessage = resultMessage + 'Amazon人數: 15' + '\n'
    resultMessage = resultMessage + '平均人數: 10.33' + '\n'
    resultMessage = resultMessage + '--------------------' + '\n'
    resultMessage = resultMessage + 'Yolo差異: 0.67' + '\n'
    resultMessage = resultMessage + 'Google差異: 5.33' + '\n'
    resultMessage = resultMessage + 'Amazon差異: 4.67' + '\n'
    resultMessage = resultMessage + '平均差異: 3.56' + '\n'
    resultMessage = resultMessage + '--------------------' + '\n'
    resultMessage = resultMessage + '警示閥值: 10' + '\n'
    resultMessage = resultMessage + '差異閥值: 5' + '\n'
    resultMessage = resultMessage + '通報層級: 業主' + '\n'
    resultMessage = resultMessage + '--------------------' + '\n'

    msgBox = QtWidgets.QMessageBox();
    msgBox.setWindowTitle('title')
    msgBox.setIconPixmap(QPixmap('1590315589-1.png').scaled(854,480, aspectRatioMode = QtCore.Qt.KeepAspectRatio))
    msgBox.setText(resultMessage)
    reply = msgBox.exec()
    