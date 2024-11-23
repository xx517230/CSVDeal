import re
import csv
import yaml
import logging

fh = logging.FileHandler("log.txt", encoding="utf-8")
sh = logging.StreamHandler()
logging.basicConfig(
    format="%(asctime)s.%(msecs)03d -%(name)s- %(levelname)s[line:%(lineno)d]-%(module)s:  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
    handlers=[fh, sh],
)


def checkFormat(file, reDict):
    re_csvHeader = re.compile(reDict["csvHeader"])
    re_csvBody = re.compile(reDict["csvBody"])
    re_dieData = re.compile(reDict["dieData"])
    dieCnt = 0
    totalNum = 0
    dieNum = 0
    dieDataCount = 0
    # 以txt文本模式打开file，并校验文件(使用正则)
    with open(file, "r", encoding="utf-8") as fp:
        for cnt, line in enumerate(fp, start=1):
            logging.debug(line.replace("\n", ""))
            if cnt == 1:
                if not re_csvHeader.search(line):
                    logging.critical(f"{file}头部格式不正确")
                continue
            match = re_csvBody.search(line)
            if match:
                totalNum = int(match.group("TotalNum"))
                dieNum = int(match.group("dieNum"))
                dieCnt += dieNum
                dieDataCount = len(re.findall(re_dieData, match.group("dieData")))
                if totalNum != dieCnt:
                    logging.critical(
                        f"{file}第{cnt}行的TotalNum与每行DieNum相加数不匹配，totalNum={totalNum}, dieCnt={dieCnt}, dieCntFront={dieCnt-dieNum}, dieNum={dieNum}"
                    )

                if dieNum != dieDataCount:
                    logging.critical(f"{file}第{cnt}行的DieNum与DieDataCount不匹配")

            else:
                logging.critical(f"{file}第{cnt}行格式不正确")


def deal(self, fileName):
    with open("regex.yaml", encoding="utf-8") as f:
        reDict = yaml.safe_load(f)
    file = self + "\\" + fileName
    checkFormat(file, reDict)
    re_csvBody = re.compile(reDict["csvBody"])
    with open(file, "r", encoding="utf-8") as fp:
        for cnt, line in enumerate(fp, start=1):
            match = re_csvBody.search(line)
            if match:
                logging.debug(line.replace("\n", ""))
                logging.debug(match.group("TotalNum"))
                logging.debug(match.group("dieNum"))
                logging.debug(match.group("dieData"))
                logging.debug(type(match.group("dieData")))
                lst = match.group("dieData").split(",")
                if lst[-1] == "":
                    lst.pop()
                logging.debug(len(lst))

    # pass


if __name__ == "__main__":
    deal(r"C:\Users\Lenovo\Desktop\t", "FA47-7697-2_20241027054724.CSV")
