'''
this script is used for summary the sell data
'''
import datetime
import sys,os
import xlrd
import xlwt
import re
from xlutils.copy import copy

class Summary:
    

    def __init__(self,dataPath = "C:/coding/test_py/data/"):
        self.path = dataPath
        self.currentDate = datetime.datetime.now().strftime('%Y-%m-%d')
        self.currentDataPath = self.path + self.currentDate + '/'
        self.titles = [['时间','单号','餐价','TB','GTB','其他价格','总价','是否刷卡'],]


    
    def write_excel_xls_append(self, value):
        #input value must be 2d list
        path = self.path
        index = len(value)  # 获取需要写入数据的行数
        workbook = xlrd.open_workbook(path)  # 打开工作簿
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
        for i in range(0, index):
            for j in range(0, len(value[i])):
                new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
        new_workbook.save(path)  # 保存工作簿
        print("Order #" + str(value[0][1]) + " written successfully")

    def read_menu(self):
        self.menu = {}

        with open('menu.txt',encoding = 'utf-8') as f:
            menu_list = f.readlines()

        for food in menu_list:
            fd = food.split(",")
            name = fd[1]
            price = float(fd[2].split("\n")[0])
            self.menu[name] = price

    def sum_total(self,path = 0):
        if path == 0:
            path = self.currentDataPath
        fileLis = os.listdir(path)
        cashTotal = 0
        cardTotal = 0
        cashCount = 0
        cardCount = 0
        cardLis = []
        for i in range(len(fileLis)):
            with open(path + fileLis[i]) as f:
                text = f.readlines()
            total = float(text[-2].split("$")[1].split("\n")[0])
            payment = text[-1]
            if payment == "Card 刷卡\n":
                cardTotal += total
                cardCount += 1
                cardLis.append([int(re.split('[#\n]',text[2])[1]),total])
                
                
            else:
                cashTotal += total
                cashCount += 1

        l = len(cardLis)
        for i in range(l):
            for j in range(l):
                if cardLis[i]>cardLis[j]:
                    cardLis[i],cardLis[j] = cardLis[j],cardLis[i]
                    
        for i in cardLis:
            print("#",i[0],"   $",i[1])

        print("cash : ",cashTotal,"   ",cashCount,"\ncard : ",cardTotal,"   ",cardCount)
        return #cashTotal,cardTotal,cashCount,cardCount


s = Summary()
s.sum_total()
