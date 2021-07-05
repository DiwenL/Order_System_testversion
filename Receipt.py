import win32api
import win32print
import tempfile
import datetime
import os,sys
import re

from Order import Order


class Receipt:
    '''
    datafile: the file address that store receipt data
    ordeNum: the number of the receipt
    orders: list that hold orders
    '''
    receiptCount = 0
    
    def __init__(self,orderLis = []):
        self.datafile = "C:\\coding\\Order_System_testversion\\data\\"
        
        self.orders = orderLis
        self.phone = None
        self.pickup = None
        self.paystat = "unpaid 未付款"
        
        currentDate = datetime.datetime.now().strftime('%Y-%m-%d')
        self.filePath = self.datafile + currentDate
        if os.path.exists(self.filePath):
            a = 0
        else:
            try:
                os.mkdir(self.filePath)
            except Exception as e:
                os.makedirs(self.filePath)

        # acquire current receipt count
        filePath = self.datafile + currentDate
        fileLis = os.listdir(filePath)
        receiptNumLis = []

        # if currently no receipt
        if len(fileLis) == 0:
            print("empty folder")
            Receipt.receiptCount = 1
            self.receiptNum = Receipt.receiptCount
            return
        
        for fileName in fileLis:
            num = int(re.split('[#.]',fileName)[1])
            receiptNumLis.append(num)
        receiptNumLis.sort()
        Receipt.receiptCount = receiptNumLis[-1]
        Receipt.receiptCount += 1
        self.receiptNum = Receipt.receiptCount
        return

    def set_phone(self,num):
        self.phone = num
        return

    def add_order(self,order):
        self.orders.append(order)
        return

    def remove_receipt(self):
        for i in range(len(self.orders)):
            self.delete_order(0)
        path = self.filePath + "\\" + "#" + str(self.receiptNum)+".txt"
        os.remove(path)
        return

    def delete_order(self,orderIdx):
        self.orders.pop(orderIdx)

    def set_pickup(self,pickup):
        self.pickup = pickup
        
    def show_receipt_brif(self):
        self.write_receipt()
        info = '#' + str(self.receiptNum) + '   ' + self.time + '\n' + '总计:                      $' + str(self.totalCost)
        return info

    def show_receipt_detail(self):
        print("======================")
        print("receipt num:"+str(self.receiptNum))
        print("----------------------")
        total = 0
        for order in self.orders:
            print(str(order.amount) + "x   " + order.name)
            if order.comments:
                for comment in order.comments:
                    print("     -" + comment)
            print("		$" + "%.2f"%order.totalCost)
            print("----------------------")
            total += order.totalCost
        print("Total		$" + "%.2f"%total)
        print(self.paystat)
        if self.phone != None:
            print(str(self.phone))
        if self.pickup != None:
            print("Pick up @ 几时取餐"+str(self.pickup))
        print("======================")
        
        
        
    def write_receipt(self):
        currentDate = datetime.datetime.now().strftime('%Y-%m-%d')
        currentTime = datetime.datetime.now().strftime('%H:%M:%S')
        self.time = currentTime
        
        receiptFile = self.filePath + "\\" + "#" + str(self.receiptNum)+".txt"

        with open(receiptFile,"w") as f:
            
            f.write("Cupar Hotel\n")
            f.write(currentDate + " " + currentTime + "\n")
            f.write("#" + str(self.receiptNum) + "\n")
            f.write("-----------------\n")
            
            total = 0
            for order in self.orders:
                f.write(str(order.amount) + "x   " + order.name + "\n")

                if order.comments:
                    for comment in order.comments:
                        f.write("     -" + comment + "\n")

                f.write("		$" + "%.2f"%order.totalCost+"\n")
                f.write("-----------------\n")
                total += order.totalCost

            f.write("Total		$" + "%.2f"%total + "\n")
            f.write(self.paystat + "\n")
            self.totalCost = total
            if self.phone != None:
                f.write(str(self.phone)+"\n")
            if self.pickup != None:
                f.write("Pick up @ 几时取餐"+str(self.pickup))

        f.close()
        return receiptFile

    def print_receipt(self):
        filename = self.write_receipt()
        print_file(filename)
        
    
def print_file(filename):
    open(filename,"r")
    win32api.ShellExecute(
        0,
        "print",
        filename,
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
        )
    return



