from PySide2.QtWidgets import QApplication, QWidget,QFileDialog,QMessageBox
from PySide2.QtCore import QStandardPaths,QDir
from Ui_CSVDeal import Ui_Form
class MyWindow(QWidget,Ui_Form):
    desktopPath = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
    fileList = []
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("文件转换工具")
        self.tbtnSelect.setDefaultAction(self.actSelect)
        self.tbtnSelect.clicked.connect(self.selectDir)
        self.tbtnDo.clicked.connect(self.convertCSV2MAP)
    def selectDir(self):
        dir = QFileDialog.getExistingDirectory(self, "选择目录",MyWindow.desktopPath)
        if dir:
            self.editDir.setText(str(dir).replace('/', '\\'))
            self.pBar.setEnabled(True)
            return 
        MessageBox = QMessageBox()
        MessageBox.critical(self, "警告", "选择的目录路径为空,请重新选择!!!") 
    def convertCSV2MAP(self):
        dir = self.editDir.text()
        if not dir:
            MessageBox = QMessageBox()
            MessageBox.critical(self, "警告", "请先选择需要转换的目录!!!")
            return
        self.fileList = QDir(dir).entryList(QDir.Files, QDir.Name)
        self.pBar.setRange(0, len(self.fileList))
        self.pBar.setValue(0)
        strTmp =""
        for file in self.fileList:
            strTmp = str(file).upper()
            if strTmp.endswith('.CSV'):
                self.pBar.setValue(self.fileList.index(file))
                print(file)
        print("*"*20)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()


