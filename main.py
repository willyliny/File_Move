from curses import window
import sys, os, shutil
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QEventLoop, QTimer, QStringListModel, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QMessageBox
from dataInterface import Ui_MainWindow

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        datatype = [r'.all', r'.txt', r'.py', r'.qft']
        
        self.cb_type.addItems(datatype)
        #click func
        self.btn_viewInput.clicked.connect(self.viewInput)
        self.btn_viewoutput.clicked.connect(self.viewOutput)
        self.btn_move.clicked.connect(self.moveFile)
        self.list_input.clicked.connect(self.onMessageBox)

    def viewInput(self):
        try:
            QMainWindow.__init__(self)
            Ui_MainWindow.__init__(self)
            inputPath = self.text_input.toPlainText()
            self.inputData = []
            print(self.cb_type.currentText())

            for i in os.listdir(inputPath):
                if self.cb_type.currentText() == r'.all':
                    self.inputData.append(i)
                else:
                    if i.endswith(self.cb_type.currentText()):
                        self.inputData.append(i)

            slm = QStringListModel()
            slm.setStringList(self.inputData)
            self.list_input.setModel(slm)
        except Exception as e:
            print(e)
            reply = QMessageBox.information(self, 'Error info ', str(e),
                QMessageBox.Ok)
    def viewOutput(self):
        try:
            QMainWindow.__init__(self)
            Ui_MainWindow.__init__(self)
            outputPath = self.text_output.toPlainText()
            outputData = []
            
            for i in os.listdir(outputPath):
                outputData.append(i)

            slm = QStringListModel()
            slm.setStringList(outputData)
            self.list_output.setModel(slm)

        except Exception as e:
            print(e)
            reply = QMessageBox.information(self, 'Error info ', str(e),
                QMessageBox.Ok)


    def moveFile(self):
        try:
            start = self.text_input.toPlainText()
            end = self.text_output.toPlainText()
            for i in self.inputData:
                print(start + '/' +i)
                shutil.move(start +'/'+i, end)
        except Exception as e:
            print(e)
            reply = QMessageBox.information(self, 'Error info ', str(e),
                QMessageBox.Ok)
            
        


    def onMessageBox(self, qModelIndex):
        try:
            self.targetFile = self.inputData[qModelIndex.row()]
            reply = QMessageBox.information(self, 'move file', 'Do you want to move?',
                QMessageBox.Yes | QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                start = self.text_input.toPlainText()
                end = self.text_output.toPlainText()
                shutil.move(start + '/' + self.targetFile  , end)
        except Exception as e:
            print(e)
            reply = QMessageBox.information(self, 'Error info ', str(e),
                QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Controller()
    # window.viewInput()
    window.show()
    sys.exit(app.exec_())