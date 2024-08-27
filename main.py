from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide2.QtCore import QStandardPaths, QDir
from Ui_CSVDeal import Ui_MyWindow
import re
import csv


class MyWindow(QWidget, Ui_MyWindow):
    desktopPath = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
    fileList = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("文件转换工具")
        self.tbtnSelect.setDefaultAction(self.actSelect)
        self.tbtnSelect.clicked.connect(self.selectDir)
        self.tbtnDo.clicked.connect(self.convertCSV2MAP)
        self.tbtnClose.clicked.connect(self.close)

    def selectDir(self):
        dir = QFileDialog.getExistingDirectory(self, "选择目录", MyWindow.desktopPath)
        if dir:
            self.editDir.setText(str(dir).replace("/", "\\"))
            self.pBar.setEnabled(True)
            return
        MessageBox = QMessageBox()
        MessageBox.critical(self, "警告", "选择的目录路径为空,请重新选择!!!")

    def timeLogDeal(self, fileName):
        re_csvHeader = re.compile(
            r"^TotalNum,DieNum,StartTime,TestTime\(S\),IntervalTime\(S\),TotalTime\(min\),(SITE,BIN,X,Y,...)?$"
        )
        # 59,5,2024/7/30 10:48:13,4.515,0.451000,1.21,11,13,84,18,12,12,84,19,13,12,84,20,14,12,84,21,15,12,84,22,
        re_csvBody = re.compile(
            r"(?P<TotalNum>^\d+),(?P<dieNum>\d{,2}),\d{4}/\d{,2}/\d{,2} \d{,2}:\d{,2}:\d{,2},[0-9.]+,[0-9.]+,[0-9.]+,(?P<dieData>(?:\d+,\d+,\d+,\d+,)+)$"
        )
        re_dieData = re.compile(r"\d+,\d+,\d+,\d+,")
        dieCnt = 0
        totalNum = 0
        dieNum = 0
        dieDataCount = 0
        file = self.editDir.text() + "\\" + fileName
        print(file)
        # 以txt文本模式打开file，并校验文件(使用正则)
        with open(file, "r") as fp:
            for cnt, line in enumerate(fp, start=1):
                print(line)
                if cnt == 1:
                    if not re_csvHeader.search(line):
                        print(f"{file}头部格式不正确")
                        return
                    continue
                match = re_csvBody.search(line)
                if match:
                    totalNum = int(match.group("TotalNum"))
                    dieNum = int(match.group("dieNum"))
                    dieCnt += dieNum
                    dieDataCount = len(re.findall(re_dieData, match.group("dieData")))
                    if totalNum != dieCnt:
                        print(
                            f"{file}第{cnt}行的TotalNum与每行DieNum相加数不匹配，totalNum={totalNum}, dieCnt={dieCnt}, dieCntFront={dieCnt-dieNum}, dieNum={dieNum}"
                        )
                        return
                    if dieNum != dieDataCount:
                        print(f"{file}第{cnt}行的DieNum与DieDataCount不匹配")
                        return
                else:
                    print(f"{file}第{cnt}行格式不正确")
                    return

        # 读取csv文件
        with open(file, "r", newline="", encoding="utf-8") as csvFile:
            csvReader = csv.reader(csvFile)
            for row in csvReader:
                print(row)
        pass

    def convertCSV2MAP(self):
        dir = self.editDir.text()
        if not dir:
            MessageBox = QMessageBox()
            MessageBox.critical(self, "警告", "请先选择需要转换的目录!!!")
            return
        self.fileList = QDir(dir).entryList(QDir.Files, QDir.Name)
        self.pBar.setRange(0, len(self.fileList))
        self.pBar.setValue(0)
        csvFiles = [file for file in self.fileList if file.upper().endswith(".CSV")]
        for file in csvFiles:
            print(file)  # 开始处理csv文件
            self.timeLogDeal(file)
            self.pBar.setValue(csvFiles.index(file) + 1)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
