# -- coding: utf-8 --
import requests
import time
import re


class EastMoneySpider:
    def request(self, page):
        dt = int(round(time.time() * 1000))
        url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page={0},200&dt={1}&atfc=&onlySale=0".format(
            page, dt)
        head = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
        }
        response = requests.get(url, headers=head)
        self.convertStr2List(response.text)

    def convertStr2List(self, resText):
        pattern = re.compile(r"datas:(.*),count")
        resStr = pattern.search(resText).group(1)
        resStr = re.sub(r"\[", '', resStr)
        resStr = re.sub(r"\]", '', resStr)
        resStrList = resStr.split(',')
        result = []
        tmpList = []
        i = 0
        for resStr in resStrList:
            tmpList.append(resStr)
            i = i + 1
            if i % 21 == 0:
                result.append(tmpList)
                tmpList = []
        print(result)


if __name__ == "__main__":
    moneySpider = EastMoneySpider()
    for page in range(1, 3):
        print("spider page{0}".format(page))
        moneySpider.request(page)
