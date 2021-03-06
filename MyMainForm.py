import sys
import time
from PyQt5.QtCore import forcepoint, right
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from menu_ui import Ui_Form
from Receipt import Receipt
from Order import Order


class MyMainForm(QMainWindow, Ui_Form):

    
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        self.btnLis1 = [self.btn1_1, self.btn1_2, self.btn1_3,
                        self.btn1_4, self.btn1_5, self.btn1_6,
                        self.btn1_7, self.btn1_8, self.btn1_9,
                        self.btn1_10,self.btn1_11,]

        self.btnLis2 = [self.btn2_1, self.btn2_2, self.btn2_3,
                        self.btn2_4, self.btn2_5, self.btn2_6,
                        self.btn2_7, self.btn2_8, self.btn2_9,
                        self.btn2_10,self.btn2_11,self.btn2_12]

        self.btnLis3 = [self.btn3_1, self.btn3_2, self.btn3_3,
                        self.btn3_4, self.btn3_5, self.btn3_6,
                        self.btn3_7, self.btn3_8, self.btn3_9,
                        self.btn3_10,self.btn3_11,self.btn3_12]
        
        self.btnLis4 = [self.btn4_1, self.btn4_2, self.btn4_3,
                        self.btn4_4, self.btn4_5, self.btn4_6,
                        self.btn4_7, self.btn4_8, self.btn4_9,
                        self.btn4_10,self.btn4_11,self.btn4_12]

        # init menu checkable and visible
        for btn in self.btnLis1:
            btn.setCheckable(True)

        for btn in self.btnLis2:
            btn.setCheckable(True)
            btn.setVisible(False)

        for btn in self.btnLis3:
            btn.setCheckable(True)
            btn.setVisible(False)

        for btn in self.btnLis4:
            btn.setCheckable(True)
            btn.setVisible(False)

        # unpay receipt list, also show in receipt list
        self.receipt_unpay = []

        #setting font for both list
        self.list_order.setFont(self.font) 
        self.list_receipt.setFont(self.font)

        #connect menu btns
        self.btn_add.clicked.connect(self.btnAddClicked)
        self.btn_sub.clicked.connect(self.btnSubClicked)
        self.btn_new.clicked.connect(self.btnNewClicked)
        self.btn_cash.clicked.connect(self.btnCashClicked)
        self.btn_card.clicked.connect(self.btnCardClicked)
        self.btn_print.clicked.connect(self.btnPrintClicked)
        self.btn_exit.clicked.connect(self.close)

        #connect btns of main menu (first list)
        self.btn1_1.clicked.connect(self.btn1_1Clicked)
        self.btn1_1.setText("??????")
        self.btn1_2.clicked.connect(self.btn1_2Clicked)
        self.btn1_2.setText("??????1")
        self.btn1_3.clicked.connect(self.btn1_3Clicked)
        self.btn1_3.setText("??????2")
        self.btn1_4.clicked.connect(self.btn1_4Clicked)
        self.btn1_4.setText("??????")
        self.btn1_5.clicked.connect(self.btn1_5Clicked)
        self.btn1_5.setText("?????? ?????????")
        self.btn1_6.clicked.connect(self.btn1_6Clicked)
        self.btn1_6.setText("?????? ??????")
        self.btn1_7.clicked.connect(self.btn1_7Clicked)
        self.btn1_7.setText("??????")
        self.btn1_8.clicked.connect(self.btn1_8Clicked)
        self.btn1_8.setText("????????????")
        self.btn1_9.clicked.connect(self.btn1_9Clicked)
        self.btn1_9.setText("???????????????")
        self.btn1_10.setVisible(False)
        self.btn1_11.setVisible(False)
        #connect btns for 2nd menu
        self.btn2_1.clicked.connect(self.btn2_1Clicked)
        self.btn2_2.clicked.connect(self.btn2_2Clicked)
        self.btn2_3.clicked.connect(self.btn2_3Clicked)
        self.btn2_4.clicked.connect(self.btn2_4Clicked)
        self.btn2_5.clicked.connect(self.btn2_5Clicked)
        self.btn2_6.clicked.connect(self.btn2_6Clicked)
        self.btn2_7.clicked.connect(self.btn2_7Clicked)
        self.btn2_8.clicked.connect(self.btn2_8Clicked)
        self.btn2_9.clicked.connect(self.btn2_9Clicked)
        self.btn2_10.clicked.connect(self.btn2_10Clicked)
        self.btn2_11.clicked.connect(self.btn2_11Clicked)
        self.btn2_12.clicked.connect(self.btn2_12Clicked)

        #connect btns for 3rd menu
        self.btn3_1.clicked.connect(self.btn3_1Clicked)
        self.btn3_2.clicked.connect(self.btn3_2Clicked)
        self.btn3_3.clicked.connect(self.btn3_3Clicked)
        self.btn3_4.clicked.connect(self.btn3_4Clicked)
        self.btn3_5.clicked.connect(self.btn3_5Clicked)
        self.btn3_6.clicked.connect(self.btn3_6Clicked)
        self.btn3_7.clicked.connect(self.btn3_7Clicked)
        self.btn3_8.clicked.connect(self.btn3_8Clicked)
        self.btn3_9.clicked.connect(self.btn3_9Clicked)
        self.btn3_10.clicked.connect(self.btn3_10Clicked)
        self.btn3_11.clicked.connect(self.btn3_11Clicked)
        self.btn3_12.clicked.connect(self.btn3_12Clicked)

        #connect btns for 4th menu
        self.btn4_1.clicked.connect(self.btn4_1Clicked)
        self.btn4_2.clicked.connect(self.btn4_2Clicked)
        self.btn4_3.clicked.connect(self.btn4_3Clicked)
        self.btn4_4.clicked.connect(self.btn4_4Clicked)
        self.btn4_5.clicked.connect(self.btn4_5Clicked)
        self.btn4_6.clicked.connect(self.btn4_6Clicked)
        self.btn4_7.clicked.connect(self.btn4_7Clicked)
        self.btn4_8.clicked.connect(self.btn4_8Clicked)
        self.btn4_9.clicked.connect(self.btn4_9Clicked)
        self.btn4_10.clicked.connect(self.btn4_10Clicked)
        self.btn4_11.clicked.connect(self.btn4_11Clicked)
        self.btn4_12.clicked.connect(self.btn4_12Clicked)

        #connect signal for showing list
        self.list_receipt.clicked.connect(self.list_receiptClicked)
        self.list_order.clicked.connect(self.list_orderClicked)


    # btn add on clicked
    def btnAddClicked(self):
        order_idx = self.list_order.currentRow()
        receipt_idx = self.list_receipt.currentRow()
        #if no order was selected
        if order_idx <= 0:
            return

        #update order amount
        current_amount = self.receipt_unpay[receipt_idx].orders[order_idx-1].amount
        self.receipt_unpay[receipt_idx].orders[order_idx-1].set_amount(current_amount+1)
        #update order list
        self.list_order.item(order_idx).setText(self.receipt_unpay[receipt_idx].orders[order_idx-1].show_order())
        self.update_receipt(receipt_idx)

    # btn sub on clicked
    def btnSubClicked(self):
        order_idx = self.list_order.currentRow()
        receipt_idx = self.list_receipt.currentRow()
        #if no order was selected
        if order_idx <= 0:
            return

        #update order amount
        current_amount = self.receipt_unpay[receipt_idx].orders[order_idx-1].amount
        #if that's the last order, delete it
        if current_amount == 1:
            self.receipt_unpay[receipt_idx].delete_order(order_idx-1)
            #update order list
            self.list_order.takeItem(order_idx)
            #update receipt
            self.update_receipt(receipt_idx)
            return
        self.receipt_unpay[receipt_idx].orders[order_idx-1].set_amount(current_amount-1)
        #update order list
        self.list_order.item(order_idx).setText(self.receipt_unpay[receipt_idx].orders[order_idx-1].show_order())
        self.update_receipt(receipt_idx)

        return
    
    # btn new on clicked
    def btnNewClicked(self):

        receipt = Receipt([])
        self.receipt_unpay.append(receipt)

        #??????????????????
        receipt_info = receipt.show_receipt_brif()
        self.list_receipt.addItem('----------------------------------\n'+receipt_info+'\n----------------------------------')
        #?????????????????????????????????
        index = self.list_receipt.count()
        self.list_receipt.setCurrentRow(index-1)

        #??????????????????
        self.clear_list_order()
        self.list_order.addItem("----------------------------------\n????????????\n----------------------------------")

        return
    
    # btn cash on clicked
    def btnCashClicked(self):
        # aquire current receipt
        receipt_idx = self.list_receipt.currentRow()
        # update receipt payment
        self.receipt_unpay[receipt_idx].paystat = "Cash ??????"
        #print the receipt
        self.receipt_unpay[receipt_idx].print_receipt()
        #remove paid receiptF
        self.list_receipt.takeItem(receipt_idx)
        self.receipt_unpay.pop(receipt_idx)
        # clear order list
        self.clear_list_order()
        return
    
    # btn card on clicked
    def btnCardClicked(self):
        # aquire current receipt
        receipt_idx = self.list_receipt.currentRow()
        # update receipt payment
        self.receipt_unpay[receipt_idx].paystat = "Card ??????"
        # print the receipt
        self.receipt_unpay[receipt_idx].print_receipt()
        # remove paid receipt
        self.list_receipt.takeItem(receipt_idx)
        self.receipt_unpay.pop(receipt_idx)
        # clear order list
        self.clear_list_order()
        return

    def btnPrintClicked(self):
        index = self.list_receipt.currentRow()
        receipt = self.receipt_unpay[index]
        receipt.print_receipt()
        return

    # Chinese food menu
    def btn1_1Clicked(self):
        self.clear_btnlist1_checked(0)
        self.clear_btnlist2_checked(-1)
        self.clear_btnlist3_checked(-1)
        self.clear_btnlist4_checked(-1)
        
        self.set_btnlist2_visible(7)
        self.set_btnlist3_visible(0)
        self.set_btnlist4_visible(0)
        
        self.btn2_1.setText("???")
        self.btn2_2.setText("??????")
        self.btn2_3.setText("??????")
        self.btn2_4.setText("??????")
        self.btn2_5.setText("??????")
        self.btn2_6.setText("??????1")
        self.btn2_7.setText("??????2")

    # fast food menu1
    def btn1_2Clicked(self):
        self.clear_btnlist1_checked(1)
        self.clear_btnlist2_checked(-1)
        self.clear_btnlist3_checked(-1)
        self.clear_btnlist4_checked(-1)
        
        self.set_btnlist2_visible(9)
        self.set_btnlist3_visible(0)
        self.set_btnlist4_visible(0)

        self.btn2_1.setText("?????????")
        self.btn2_2.setText("??????")
        self.btn2_3.setText("??????")
        self.btn2_4.setText("??????")
        self.btn2_5.setText("??????")
        self.btn2_6.setText("?????????")
        self.btn2_7.setText("?????????")
        self.btn2_8.setText("??????")
        self.btn2_9.setText("????????????")

    # fast food menu2
    def btn1_3Clicked(self):
        
        self.clear_btnlist1_checked(2)
        self.clear_btnlist2_checked(-1)
        self.clear_btnlist3_checked(-1)
        self.clear_btnlist4_checked(-1)
        
        self.set_btnlist2_visible(8)
        self.set_btnlist3_visible(0)
        self.set_btnlist4_visible(0)

        self.btn2_1.setText("????????????")
        self.btn2_2.setText("??????")
        self.btn2_3.setText("?????????")
        self.btn2_4.setText("?????????")
        self.btn2_5.setText("??????2???")
        self.btn2_6.setText("??????5???")
        self.btn2_7.setText("??????1???")
        self.btn2_8.setText("??????4???")

    # combo menu
    def btn1_4Clicked(self):
        
        self.clear_btnlist1_checked(3)
        self.clear_btnlist2_checked(-1)
        self.clear_btnlist3_checked(-1)
        self.clear_btnlist4_checked(-1)
        
        self.set_btnlist2_visible(7)
        self.set_btnlist3_visible(0)
        self.set_btnlist4_visible(0)

        self.btn2_1.setText("????????????")
        self.btn2_2.setText("????????????")
        self.btn2_3.setText("????????????")
        self.btn2_4.setText("????????????")
        self.btn2_5.setText("????????????")
        self.btn2_6.setText("????????????")
        self.btn2_7.setText("????????????")
        return

    # black btl beer menu
    def btn1_5Clicked(self):
        
        self.clear_btnlist1_checked(4)
        self.clear_btnlist2_checked(-1)
        self.clear_btnlist3_checked(-1)
        self.clear_btnlist4_checked(-1)
        
        self.set_btnlist2_visible(11)
        self.set_btnlist3_visible(0)
        self.set_btnlist4_visible(0)

        self.btn2_1.setText("Kokanee")
        self.btn2_2.setText("Bud Weiser")
        self.btn2_3.setText("Bud Light")
        self.btn2_4.setText("Coors Light")
        self.btn2_5.setText("Canadian")
        self.btn2_6.setText("Bohemian")
        self.btn2_7.setText("Pilsner")
        self.btn2_8.setText("Calgary")
        self.btn2_9.setText("OV")
        self.btn2_10.setText("Forager")
        self.btn2_11.setText("??????")

    # other beer menu
    def btn1_6Clicked(self):
        
        self.clear_btnlist1_checked(5)
        self.clear_btnlist2_checked(-1)
        self.clear_btnlist3_checked(-1)
        self.clear_btnlist4_checked(-1)
        
        self.set_btnlist2_visible(5)
        self.set_btnlist3_visible(0)
        self.set_btnlist4_visible(0)

        self.btn2_1.setText("Original 16")
        self.btn2_2.setText("Corona")
        self.btn2_3.setText("Heineken")
        self.btn2_4.setText("Millers Highlight")
        self.btn2_5.setText("Millers Black")
        self.btn2_6.setText("Labatt Lite")

    # wine menu
    def btn1_7Clicked(self):
        self.clear_btnlist1_checked(6)
        self.clear_btnlist2_checked(-1)
        self.clear_btnlist3_checked(-1)
        self.clear_btnlist4_checked(-1)

        self.set_btnlist2_visible(7)
        self.set_btnlist3_visible(12)
        self.set_btnlist4_visible(0)

        self.btn2_1.setText("shot 6")
        self.btn2_2.setText("shot 8")
        self.btn2_3.setText("shot 10")
        self.btn2_4.setText("cocktail 6")
        self.btn2_5.setText("cocktail 8")
        self.btn2_6.setText("cocktail 10")
        self.btn2_7.setText("cocktail 12")
        self.btn2_8.setText("")
        self.btn2_9.setText("")
        self.btn2_10.setText("")
        self.btn2_11.setText("")
        self.btn2_12.setText("")

        self.btn3_1.setText("Smirnoff 375ml")
        self.btn3_2.setText("Smirnoff 750ml")
        self.btn3_3.setText("Smirnoff 1.14L")
        self.btn3_4.setText("Smirnoff 1.75L")
        self.btn3_5.setText("Wiser's 375ml")
        self.btn3_6.setText("Wiser's 750ml")
        self.btn3_7.setText("Wiser's 1.14L")
        self.btn3_8.setText("Wiser's 1.75L")
        self.btn3_9.setText("Captain 375ml")
        self.btn3_10.setText("Captain 750ml")
        self.btn3_11.setText("Captain 1.14L")
        self.btn3_12.setText("Captain 1.75L")
    
    # cig and other menu
    def btn1_8Clicked(self):
        self.clear_btnlist1_checked(7)
        self.clear_btnlist2_checked(-1)
        self.clear_btnlist3_checked(-1)
        self.clear_btnlist4_checked(-1)

        self.set_btnlist2_visible(9)
        self.set_btnlist3_visible(0)
        self.set_btnlist4_visible(0)

        self.btn2_1.setText("pop 2")
        self.btn2_2.setText("pop 4")
        self.btn2_3.setText("?????????")
        self.btn2_4.setText("?????????")
        self.btn2_5.setVisible(False)
        self.btn2_6.setText("cig 20")
        self.btn2_7.setText("cig 18")
        self.btn2_8.setVisible(False)
        self.btn2_9.setText("??????")

    # premake cocktail menu
    def btn1_9Clicked(self):
        self.clear_btnlist1_checked(8)
        self.clear_btnlist2_checked(-1)
        self.clear_btnlist3_checked(-1)
        self.clear_btnlist4_checked(-1)

        self.set_btnlist2_visible(10)
        self.set_btnlist3_visible(10)
        self.set_btnlist4_visible(0)

        self.btn2_1.setText("Twisted Tea")
        self.btn2_2.setText("American Vintage")
        self.btn2_3.setText("Plam Bay")
        self.btn2_4.setText("Nutrl")
        self.btn2_5.setText("Hey Yall")
        self.btn2_6.setText("Smirnoff Ice (???)")
        self.btn2_7.setText("Smirnoff Ice (???)")
        self.btn2_8.setText("Mike's")
        self.btn2_9.setText("Tempo")
        self.btn2_10.setText("2L ??????")

        self.btn3_1.setText("Smirnoff Ice (???)")
        self.btn3_2.setText("Smirnoff saeser (???)")
        self.btn3_3.setText("Truly")
        self.btn3_4.setText("Berry Blast (???)")
        self.btn3_5.setText("Berry Blast (???)")
        self.btn3_6.setText("Ultra")
        self.btn3_7.setText("Rebellion")
        self.btn3_8.setText("Smirnoff Sangria")
        self.btn3_9.setText("White Claw")
        self.btn3_10.setText("Black Fly")

    def btn2_1Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(0)
        self.clear_btnlist3_checked(-1)
        #??????????????????
        text = self.btn2_1.text()
        
        #?????????
        if text == "???":
            self.set_btnlist3_visible(2)

            self.btn3_1.setText("?????????")
            self.btn3_2.setText("?????????")

        #??????1?????????2??????
        if text == "?????????" or text == "????????????":
            self.set_btnlist3_visible(9)
            
            self.show_favour_menu()

        #????????????
        if text == "????????????":
            self.set_btnlist3_visible(4)
            #????????????????????????????????????
            self.btn3_1.setText("A")
            self.btn3_2.setText("B")
            self.btn3_3.setText("C")
            self.btn3_4.setText("D")

        # beer
        if text == "Kokanee" or text == "Original 16":
            self.show_beer_amount()

        # other
        if text == "pop 2":
            self.addOrder(Order("pop",2))
               
        #premake cocktail
        if text == "Twisted Tea":
            self.show_premake_cocktail_amount()

        if text == "shot 6":
            self.addOrder(Order("shot",6))

    def btn2_2Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(1)
        self.clear_btnlist3_checked(-1)
        
        text = self.btn2_2.text()
        if text == "??????":
            self.show_meet_menu()

        if text == "??????" or text == "??????":
            self.set_btnlist3_visible(9)
            self.show_favour_menu()

        if text == "????????????":
            self.set_btnlist3_visible(0)
            self.addOrder(Order("????????????",28.99))
        
        # beer
        if text == "Bud Weiser" or text == "Corona":
            self.show_beer_amount()

        # other
        if text == "pop 4":
            self.addOrder(Order("pop 2L",4))

        # premake cocktail
        if text == "American Vintage":
            self.show_premake_cocktail_amount()
        
        #cocktail
        if text == "shot 8":
            self.addOrder(Order("shot",8))

    def btn2_3Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(2)
        self.clear_btnlist3_checked(-1)
        
        text = self.btn2_3.text()
        if text == "??????":
            self.show_meet_menu()
            
        if text == "??????" or text == "?????????":
            self.set_btnlist3_visible(9)
            self.show_favour_menu()
            
        if text == "????????????":
            self.set_btnlist3_visible(0)
            self.addOrder(Order("????????????",39.99))

        # beer
        if text == "Bud Light" or text == "Heineken":
            self.show_beer_amount()

        if text == "?????????":
            self.addOrder(Order("Clamato",5))

        if text == "Plam Bay":
            self.show_premake_cocktail_amount()

        if text == "shot 10":
            self.addOrder(Order("shot",10))

    def btn2_4Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(3)
        self.clear_btnlist3_checked(-1)
        
        text = self.btn2_4.text()
        if text == "??????":
            self.show_meet_menu()

        if text == "??????" or text == "?????????":
            self.set_btnlist3_visible(9)
            self.show_favour_menu()

        if text == "????????????":
            self.set_btnlist3_visible(0)
            self.addOrder(Order("????????????",55.99))

        # beer
        if text == "Coors Light" or text == "Millers Highlight":
            self.show_beer_amount()

        if text == "?????????":
            self.addOrder(Order("?????????",3.5))

        if text == "Nutrl":
            self.show_premake_cocktail_amount()

        if text == "cocktail 6":
            self.addOrder(Order("cocktail",6))

    def btn2_5Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(4)
        self.clear_btnlist3_checked(-1)
        
        text = self.btn2_5.text()
        if text == "??????":
            self.show_meet_menu()

        if text == "??????" or text == "??????2???":
            self.set_btnlist3_visible(9)
            self.show_favour_menu()

        if text == "????????????":
            self.set_btnlist3_visible(0)
            self.addOrder(Order("????????????",68.99))

        # beer
        if text == "Canadian" or text == "Millers Black":
            self.show_beer_amount()

        if text == "Hey Yall":
            self.show_premake_cocktail_amount()

        if text == "cocktail 8":
            self.addOrder(Order("cocktail",8))

    def btn2_6Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(5)
        self.clear_btnlist3_checked(-1)
        
        text = self.btn2_6.text()
        if text == "??????1":
            self.set_btnlist3_visible(6)

            self.btn3_1.setText("???????????????")
            self.btn3_2.setText("?????????")
            self.btn3_3.setText("?????????")
            self.btn3_4.setText("?????????")
            self.btn3_5.setText("?????????")
            self.btn3_6.setText("????????????")

        if text == "?????????" or text == "??????5???":
            self.set_btnlist3_visible(9)
            self.show_favour_menu()
        
        if text == "????????????":
            self.set_btnlist3_visible(0)
            self.addOrder(Order("????????????",88.99))
            
        # beer
        if text == "Bohemian":
            self.show_beer_amount()

        if text == "cig 20":
            self.addOrder(Order("cig 20",20))
        
        if text == "Smirnoff Ice (???)":
            self.show_premake_cocktail_amount()

        if text == "cocktail 10":
            self.addOrder(Order("cocktail",10))

    def btn2_7Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(6)
        self.clear_btnlist3_checked(-1)
        
        text = self.btn2_7.text()
        if text == "??????2":
            self.set_btnlist3_visible(7)

            self.btn3_1.setText("?????????")
            self.btn3_2.setText("?????????")
            self.btn3_3.setText("?????????")
            self.btn3_4.setText("?????????")
            self.btn3_5.setText("?????????")
            self.btn3_6.setText("????????????")
            self.btn3_7.setText("?????????")
            
        if text == "????????????" or text == "??????1???":
            self.set_btnlist3_visible(9)
            self.show_favour_menu()
            
        if text == "????????????":
            self.set_btnlist3_visible(0)
            self.addOrder(Order("????????????",109.99))

        # beer
        if text == "Pilsner":
            self.show_beer_amount()

        if text == "cig 18":
            self.addOrder(Order("cig 18",18))

        if text == "Smirnoff Ice (???)":
            self.show_premake_cocktail_amount()

        if text == "cocktail 12":
            self.addOrder(Order("cocktail",12))

    def btn2_8Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(7)
        self.clear_btnlist3_checked(-1)

        text = self.btn2_8.text()
        if text == "??????" or text == "??????4???":
            self.set_btnlist3_visible(9)
            self.show_favour_menu()

        # beer
        if text == "Calgary":
            self.show_beer_amount()

        if text == "Mike's":
            self.clear_btnlist3_checked(-1)
            self.show_premake_cocktail_amount()

    def btn2_9Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(8)
        self.clear_btnlist3_checked(-1)
        
        text = self.btn2_9.text()
        if text == "????????????":
            self.set_btnlist3_visible(9)
            self.show_favour_menu()

        # beer
        if text == "OV":
            self.show_beer_amount()

        if text == "??????":
            self.addOrder(Order("??????",1))

        if text == "Tempo":
            self.show_premake_cocktail_amount()

    def btn2_10Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(9)
        self.clear_btnlist3_checked(-1)
        text = self.btn2_10.text()

        #beer
        if text == "Forager":
            self.show_beer_amount()

        if text == "2L ??????":
            self.clear_btnlist3_checked(-1)
            self.show_premake_cocktail_amount()

    def btn2_11Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist2_checked(10)
        self.clear_btnlist3_checked(-1)
        text = self.btn2_11.text()

        #beer
        if text == "??????":
            self.show_beer_amount()
        return

    def btn2_12Clicked(self):
        return

    def btn3_1Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(0)
        text3 = self.btn3_1.text()
         
        if text3 == "?????????":
            self.addOrder(Order("?????????",8.5))

        if text3 == "???":
            if self.btn2_2.isChecked():
                self.addOrder(Order("?????????",8.50))
            elif self.btn2_3.isChecked():
                self.addOrder(Order("?????????",11.99))
            elif self.btn2_4.isChecked():
                self.addOrder(Order("?????????",9.99))
            elif self.btn2_5.isChecked():
                self.addOrder(Order("?????????",9.99))
                
        if text3 == "A":
            self.addOrder(Order("A??????",15.99))

        if text3 == '???????????????':
            self.addOrder(Order("???????????????",11.99))

        if text3 == "?????????":
            self.addOrder(Order("?????????",11.99))

        if text3 == "???":
            self.addFastFood('')

        if text3 == "24can":
            if self.btn1_5.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Kokanee",59,comment="24can"))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Bud Weiser",59,comment="24can"))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Bud Light",59,comment="24can"))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Coors Light",59,comment="24can"))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Canadian",59,comment="24can"))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Bohemian",49,comment="24can"))
                elif self.btn2_7.isChecked():
                    self.addOrder(Order("Pilsner",51,comment="24can"))
                elif self.btn2_8.isChecked():
                    print("no such item")
                elif self.btn2_9.isChecked():
                    print("no such item")
                elif self.btn2_10.isChecked():
                    print("no such item")
                elif self.btn2_11.isChecked():
                    self.addOrder(Order("Other beer",59,comment="24can"))

            # other beer menu
            if self.btn1_6.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Original 16",75,comment=text3))
                elif self.btn2_2.isChecked():
                    print("no such item")
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Heineken",81,comment=text3))
                elif self.btn2_4.isChecked():
                    print("no such item")
                elif self.btn2_5.isChecked():
                    print("no such item")
                elif self.btn2_6.isChecked():
                    print("no such item")
        
        if text3 == "Smirnoff Ice (???)":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Smirnoff 375ml":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Smirnoff",18,comment="375ml"))

        return

    def btn3_2Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(1)        
        text3 = self.btn3_2.text()
        
        if text3 == "?????????":
            self.addOrder(Order("?????????",13.99))

        if text3 == "???":
            if self.btn2_2.isChecked():
                self.addOrder(Order("?????????",9.99))
            elif self.btn2_3.isChecked():
                self.addOrder(Order("?????????",11.99))
            elif self.btn2_4.isChecked():
                self.addOrder(Order("?????????",10.99))
            elif self.btn2_5.isChecked():
                self.addOrder(Order("?????????",10.99))

        if text3 == "B":
            self.addOrder(Order("B??????",15.59))

        if text3 == "?????????":
            self.addOrder(Order("?????????",11.99))

        if text3 == "?????????":
            self.addOrder(Order("?????????",11.99))

        if text3 == "18can":
            if self.btn1_5.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Kokanee",46,comment="18can"))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Bud Weiser",46,comment="18can"))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Bud Light",46,comment="18can"))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Coors Light",46,comment="18can"))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Canadian",46,comment="18can"))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Bohemian",39,comment="18can"))
                elif self.btn2_7.isChecked():
                    self.addOrder(Order("Pilsner",40,comment="18can"))
                elif self.btn2_8.isChecked():
                    print("no such item")
                elif self.btn2_9.isChecked():
                    print("no such item")
                elif self.btn2_10.isChecked():
                    print("no such item")
                elif self.btn2_11.isChecked():
                    self.addOrder(Order("Other beer",46,comment="18can"))
            
            # other beer menu
            if self.btn1_6.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Original 16",57,comment=text3))
                elif self.btn2_2.isChecked():
                    print("no such item")
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Heineken",61,comment=text3))
                elif self.btn2_4.isChecked():
                    print("no such item")
                elif self.btn2_5.isChecked():
                    print("no such item")
                elif self.btn2_6.isChecked():
                    print("no such item")
        
        if text3 == "Smirnoff saeser (???)":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Smirnoff 750ml":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Smirnoff",31,comment="750ml"))

        return

    def btn3_3Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(2)
        text3 = self.btn3_3.text()
        
        if text3 == "???":
            if self.btn2_2.isChecked():
                self.addOrder(Order("?????????",10.99))
            elif self.btn2_3.isChecked():
                self.addOrder(Order("?????????",11.99))
            elif self.btn2_4.isChecked():
                self.addOrder(Order("?????????",11.99))
            elif self.btn2_5.isChecked():
                self.addOrder(Order("?????????",11.99))

        if text3 == "C":
            self.addOrder(Order("C??????",14.99))

        if text3 == "?????????":
            self.addOrder(Order("?????????",10.99))

        if text3 == "?????????":
            self.addOrder(Order("?????????",9.99))

        if text3 == "A ??????":
            self.addFastFood(text3)

        if text3 == "12can":
            if self.btn1_5.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Kokanee",32,comment="12can"))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Bud Weiser",32,comment="12can"))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Bud Light",32,comment="12can"))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Coors Light",32,comment="12can"))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Canadian",32,comment="12can"))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Bohemian",29,comment="12can"))
                elif self.btn2_7.isChecked():
                    self.addOrder(Order("Pilsner",29,comment="12can"))
                elif self.btn2_8.isChecked():
                    print("no such item")
                elif self.btn2_9.isChecked():
                    print("no such item")
                elif self.btn2_10.isChecked():
                    print("no such item")
                elif self.btn2_11.isChecked():
                    self.addOrder(Order("Other beer",32,comment="12can"))
            
            # other beer menu
            if self.btn1_6.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Original 16",39,comment=text3))
                elif self.btn2_2.isChecked():
                    print("no such item")
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Heineken",42,comment=text3))
                elif self.btn2_4.isChecked():
                    print("no such item")
                elif self.btn2_5.isChecked():
                    print("no such item")
                elif self.btn2_6.isChecked():
                    print("no such item")
        
        if text3 == "Truly":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Smirnoff 1.14L":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Smirnoff",45,comment="1.14L"))

        return

    def btn3_4Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(3)
        text3 = self.btn3_4.text()
        
        if text3 == "???":
            if self.btn2_2.isChecked():
                self.addOrder(Order("?????????",9.50))
            elif self.btn2_3.isChecked():
                self.addOrder(Order("?????????",10.99))
            elif self.btn2_4.isChecked():
                self.addOrder(Order("?????????",10.99))
            elif self.btn2_5.isChecked():
                self.addOrder(Order("?????????",9.99))

        if text3 == "D":
            self.addOrder(Order("D??????",15.59))

        if text3 == "?????????":
            self.addOrder(Order("?????????",13.99))

        if text3 == "?????????":
            self.addOrder(Order("?????????",12.99))

        if text3 == "B ??????":
            self.addFastFood(text3)

        if text3 == "6can":
            if self.btn1_5.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Kokanee",18,comment="6can"))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Bud Weiser",18,comment="6can"))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Bud Light",18,comment="6can"))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Coors Light",18,comment="6can"))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Canadian",18,comment="6can"))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Bohemian",18,comment="6can"))
                elif self.btn2_7.isChecked():
                    self.addOrder(Order("Pilsner",18,comment="6can"))
                elif self.btn2_8.isChecked():
                    print("no such item")
                elif self.btn2_9.isChecked():
                    print("no such item")
                elif self.btn2_10.isChecked():
                    self.addOrder(Order("Forager",24,comment=text3))
                elif self.btn2_11.isChecked():
                    self.addOrder(Order("Other beer",18,comment="6can"))
        # other beer menu
            if self.btn1_6.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Original 16",20,comment=text3))
                elif self.btn2_2.isChecked():
                    print("no such item")
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Heineken",22,comment=text3))
                elif self.btn2_4.isChecked():
                    print("no such item")
                elif self.btn2_5.isChecked():
                    print("no such item")
                elif self.btn2_6.isChecked():
                    print("no such item")
        
        if text3 == "Berry Blast (???)":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Smirnoff 1.75L":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Smirnoff",62,comment="1.75L"))

        return

    def btn3_5Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(4)
        text3 = self.btn3_5.text()
        
        if text3 == "??????":
            if self.btn2_2.isChecked():
                self.addOrder(Order("????????????",10.99))
            elif self.btn2_3.isChecked():
                self.addOrder(Order("????????????",11.99))
            elif self.btn2_4.isChecked():
                self.addOrder(Order("????????????",12.99))
            elif self.btn2_5.isChecked():
                self.addOrder(Order("????????????",11.99))

        if text3 == "?????????":
            self.addOrder(Order("?????????",12.99))

        if text3 == "?????????":
            self.addOrder(Order("?????????",11.99))

        if text3 == "C buffalo":
            self.addFastFood(text3)

        if text3 == "24btl":
            if self.btn1_5.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Kokanee",69,comment="24btl"))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Bud Weiser",69,comment="24btl"))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Bud Light",69,comment="24btl"))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Coors Light",69,comment="24btl"))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Canadian",69,comment="24btl"))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Bohemian",66,comment="24btl"))
                elif self.btn2_7.isChecked():
                    self.addOrder(Order("Pilsner",66,comment="24btl"))
                elif self.btn2_8.isChecked():
                    self.addOrder(Order("Calgary",63,comment="24btl"))
                elif self.btn2_9.isChecked():
                    self.addOrder(Order("OV",70,comment="24btl"))
                elif self.btn2_10.isChecked():
                    self.addOrder(Order("Forager",98,comment="24btl"))
                elif self.btn2_11.isChecked():
                    self.addOrder(Order("Other beer",69,comment="24btl"))
            # other beer menu
            if self.btn1_6.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Original 16",67,comment=text3))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Corona",67,comment=text3))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Heineken",85,comment=text3))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Miller Highlight",69,comment=text3))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Millers Black",69,comment=text3))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Labatt Lite",66,comment=text3))
        
        if text3 == "Berry Blast (???)":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Wiser's 375ml":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Wiser's",16,comment="375ml"))

        return

    def btn3_6Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(5)
        text3 = self.btn3_6.text()

        if text3 == "????????????":
            self.addOrder(Order("????????????",11.99))

        if text3 == "????????????":
            self.addOrder(Order("????????????",13.99))

        if text3 == "D ??????":
            self.addFastFood(text3)

        if text3 == "12btl":
            if self.btn1_5.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Kokanee",38,comment="12btl"))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Bud Weiser",38,comment="12btl"))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Bud Light",38,comment="12btl"))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Coors Light",38,comment="12btl"))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Canadian",38,comment="12btl"))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Bohemian",34,comment="12btl"))
                elif self.btn2_7.isChecked():
                    self.addOrder(Order("Pilsner",35,comment="12btl"))
                elif self.btn2_8.isChecked():
                    self.addOrder(Order("Calgary",33,comment="12btl"))
                elif self.btn2_9.isChecked():
                    self.addOrder(Order("OV",36,comment="12btl"))
                elif self.btn2_10.isChecked():
                    self.addOrder(Order("Forager",50,comment="12btl"))
            
            # other beer menu
            if self.btn1_6.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Original 16",36,comment=text3))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Corona",39,comment=text3))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Heineken",44,comment=text3))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Miller Highlight",39,comment=text3))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Millers Black",39,comment=text3))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Labatt Lite",36,comment=text3))

        if text3 == "Ultra":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Wiser's 750ml":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Wiser's",30,comment="750ml"))

        return

    def btn3_7Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(6)
        text3 = self.btn3_7.text()
        if text3 == "?????????":
            self.addOrder(Order("?????????",14.99))

        if text3 == "E ranch":
            self.addFastFood(text3)

        if text3 == "6btl":
            if self.btn1_5.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Kokanee",22,comment=text3))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Bud Weiser",22,comment=text3))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Bud Light",22,comment=text3))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Coors Light",22,comment=text3))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Canadian",22,comment=text3))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Bohemian",19,comment=text3))
                elif self.btn2_7.isChecked():
                    self.addOrder(Order("Pilsner",19,comment=text3))
                elif self.btn2_8.isChecked():
                    self.addOrder(Order("Calgary",19,comment=text3))
                elif self.btn2_9.isChecked():
                    self.addOrder(Order("OV",19,comment=text3))
                elif self.btn2_10.isChecked():
                    self.addOrder(Order("Forager",26,comment=text3))
                elif self.btn2_11.isChecked():
                    self.addOrder(Order("Other",22,comment=text3))

            # other beer menu
            if self.btn1_6.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Original 16",22,comment=text3))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Corona",23,comment=text3))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Heineken",23,comment=text3))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Miller Highlight",23,comment=text3))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Millers Black",23,comment=text3))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Labatt Lite",22,comment=text3))
        
        if text3 == "Rebellion":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Wiser's 1.14L":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Wiser's",43,comment="1.14L"))

    def btn3_8Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(7)
        text3 = self.btn3_8.text()

        if text3 == "F ??????":
            self.addFastFood(text3)

        if text3 == "Smirnoff Sangria":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Wiser's 1.75L":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Wiser's",59,comment="1.75L"))

        if text3 == "15can":
            if self.btn1_5.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Kokanee",40,comment=text3))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Bud Weiser",40,comment=text3))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Bud Light",40,comment=text3))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Coors Light",40,comment=text3))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Canadian",40,comment=text3))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Bohemian",36,comment=text3))
                elif self.btn2_7.isChecked():
                    self.addOrder(Order("Pilsner",36,comment=text3))
                elif self.btn2_8.isChecked():
                    print("no such option")
                elif self.btn2_9.isChecked():
                    print("no such option")
                elif self.btn2_10.isChecked():
                    print("no such option")
                elif self.btn2_11.isChecked():
                    print("no such option")

            # other beer menu
            if self.btn1_6.isChecked():
                if self.btn2_1.isChecked():
                    print("no such option")
                elif self.btn2_2.isChecked():
                    print("no such option")
                elif self.btn2_3.isChecked():
                    print("no such option")
                elif self.btn2_4.isChecked():
                    print("no such option")
                elif self.btn2_5.isChecked():
                    print("no such option")
                elif self.btn2_6.isChecked():
                    print("no such option")
        
        return

    def btn3_9Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(8)
        text3 = self.btn3_9.text()

        if text3 == "G ??????":
            self.addFastFood(text3)

        if text3 == "1TB":
            # black btl beer selection
            if self.btn1_5.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Kokanee",6,comment=text3))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Bud Weiser",6,comment=text3))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Bud Light",6,comment=text3))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Coors Light",6,comment=text3))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Canadian",6,comment=text3))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Bohemian",6,comment=text3))
                elif self.btn2_7.isChecked():
                    self.addOrder(Order("Pilsner",6,comment=text3))
                elif self.btn2_8.isChecked():
                    self.addOrder(Order("Calgary",6,comment=text3))
                elif self.btn2_9.isChecked():
                    self.addOrder(Order("OV",6,comment=text3))
                elif self.btn2_10.isChecked():
                    self.addOrder(Order("Forager",6,comment=text3))
                elif self.btn2_11.isChecked():
                    self.addOrder(Order("Other",6,comment=text3))
            
            # other beer menu
            if self.btn1_6.isChecked():
                if self.btn2_1.isChecked():
                    self.addOrder(Order("Original 16",6.75,comment=text3))
                elif self.btn2_2.isChecked():
                    self.addOrder(Order("Corona",6.75,comment=text3))
                elif self.btn2_3.isChecked():
                    self.addOrder(Order("Heineken",6.75,comment=text3))
                elif self.btn2_4.isChecked():
                    self.addOrder(Order("Miller Highlight",6.75,comment=text3))
                elif self.btn2_5.isChecked():
                    self.addOrder(Order("Millers Black",6.75,comment=text3))
                elif self.btn2_6.isChecked():
                    self.addOrder(Order("Labatt Lite",6.75,comment=text3))

        
        if text3 == "White Claw":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Captain 375ml":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Captain",19,comment="375ml"))

        return

    def btn3_10Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(9)
        text3 = self.btn3_10.text()

        if text3 == "H ????????????":
            self.addFastFood(text3)
        
        if text3 == "Black Fly":
            self.clear_btnlist2_checked(-1)
            self.show_premake_cocktail_amount()

        if text3 == "Captain 750ml":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Captain",35,comment="750ml"))

        return

    def btn3_11Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(10)
        text3 = self.btn3_11.text()

        if text3 == "I greek":
            self.addFastFood(text3)

        if text3 == "Captain 1.14L":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Captain",50,comment="1.14L"))
        
        return

    def btn3_12Clicked(self):
        self.clear_btnlist4_checked(-1)
        self.clear_btnlist3_checked(11)
        text3 = self.btn3_12.text()

        if text3 == "J ???????????????":
            self.addFastFood(text3)

        if text3 == "Captain 1.75L":
            self.clear_btnlist2_checked(-1)
            self.addOrder(Order("Captain",69,comment="1.75L"))
        
        return

    def btn4_1Clicked(self):
        self.clear_btnlist4_checked(0)
        
        for btn in self.btnLis2:
            if btn.isChecked():
                price = 68
                if btn.text() == "Smirnoff Ice (???)":
                    price = 98
                if btn.text() == "2L ??????":
                    print("no such item")
                    return
                self.addOrder(Order(btn.text(),price))
                return
        for btn in self.btnLis3:
            if btn.isChecked():
                price = 68
                if btn.text() == "Berry Blast (???)" or btn.text() == "Smirnoff Sangria" or btn.text() == "Black Fly": 
                    price = 98
                self.addOrder(Order(btn.text(),price))
                return

    def btn4_2Clicked(self):
        self.clear_btnlist4_checked(1)
        
        for btn in self.btnLis2:
            if btn.isChecked():
                price = 53
                if btn.text() == "Smirnoff Ice (???)":
                    price = 74
                if btn.text() == "2L ??????":
                    print("no such item")
                    return
                self.addOrder(Order(btn.text(),price))
                return
        for btn in self.btnLis3:
            if btn.isChecked():
                price = 53
                if btn.text() == "Berry Blast (???)" or btn.text() == "Smirnoff Sangria" or btn.text() == "Black Fly": 
                    price = 74
                self.addOrder(Order(btn.text(),price))
                return
                
    def btn4_3Clicked(self):
        self.clear_btnlist4_checked(2)
        
        for btn in self.btnLis2:
            if btn.isChecked():
                price = 36
                if btn.text() == "Smirnoff Ice (???)":
                    price = 50
                if btn.text() == "2L ??????":
                    print("no such item")
                    return
                self.addOrder(Order(btn.text(),price))
                return
        for btn in self.btnLis3:
            if btn.isChecked():
                price = 36
                if btn.text() == "Berry Blast (???)" or btn.text() == "Smirnoff Sangria" or btn.text() == "Black Fly": 
                    price = 50
                self.addOrder(Order(btn.text(),price))
                return

    def btn4_4Clicked(self):
        self.clear_btnlist4_checked(3)
        
        for btn in self.btnLis2:
            if btn.isChecked():
                price = 20
                if btn.text() == "Smirnoff Ice (???)":
                    price = 26
                if btn.text() == "2L ??????":
                    print("no such item")
                    return
                self.addOrder(Order(btn.text(),price))
                return
        for btn in self.btnLis3:
            if btn.isChecked():
                price = 20
                if btn.text() == "Berry Blast (???)" or btn.text() == "Smirnoff Sangria" or btn.text() == "Black Fly": 
                    price = 30
                self.addOrder(Order(btn.text(),price))
                return

    def btn4_5Clicked(self):
        self.clear_btnlist4_checked(4)
        
        for btn in self.btnLis2:
            if btn.isChecked():
                    price = 4
                    if btn.text() == "Smirnoff Ice (???)":
                        price = 6
                    if btn.text() == "2L ??????":
                        self.addOrder(Order("2L ??????",15))
                        return
                    self.addOrder(Order(btn.text(),price))
                    return
        for btn in self.btnLis3:
            if btn.isChecked():
                price = 4                    
                if btn.text() == "Berry Blast (???)" or btn.text() == "Smirnoff Sangria" or btn.text() == "Black Fly": 
                    price = 6
                self.addOrder(Order(btn.text(),price))
                return
                
    def btn4_6Clicked(self):
        return

    def btn4_7Clicked(self):
        self.clear_btnlist4_checked(6)
        
        for btn in self.btnLis2:
            if btn.isChecked():
                price = 6.75
                if btn.text() == "Smirnoff Ice (???)":
                    price = 8
                if btn.text() == "2L ??????":
                    print("no such item")
                    return
                self.addOrder(Order(btn.text(),price))
                return

        for btn in self.btnLis3:
            if btn.isChecked():
                price = 6.75
                if btn.text() == "Berry Blast (???)" or btn.text() == "Smirnoff Sangria" or btn.text() == "Black Fly": 
                    price = 8
                self.addOrder(Order(btn.text(),price))
                return 
        
    def btn4_8Clicked(self):
        return        

    def btn4_9Clicked(self):
        return  

    def btn4_10Clicked(self):
        return  

    def btn4_11Clicked(self):
        return   

    def btn4_12Clicked(self):
        return

    def clear_check_btn(self,lisNum):
        if lisNum == 1:
            self.btn1_1.setCheckable(False)

    def show_meet_menu(self):
        self.set_btnlist3_visible(5)

        self.btn3_1.setText("???")
        self.btn3_2.setText("???")
        self.btn3_3.setText("???")
        self.btn3_4.setText("???")
        self.btn3_5.setText("??????")
        
    def show_favour_menu(self):
        self.set_btnlist3_visible(12)
        
        self.btn3_1.setText("???")
        self.btn3_2.setVisible(False)
        self.btn3_3.setText("A ??????")
        self.btn3_4.setText("B ??????")
        self.btn3_5.setText("C buffalo")
        self.btn3_6.setText("D ??????")
        self.btn3_7.setText("E ranch")
        self.btn3_8.setText("F ??????")
        self.btn3_9.setText("G ??????")
        self.btn3_10.setText("H ????????????")
        self.btn3_11.setText("I greek")
        self.btn3_12.setText("J ???????????????")
          
    def show_beer_amount(self):
        self.set_btnlist3_visible(9)

        self.btn3_1.setText("24can")
        self.btn3_2.setText("18can")
        self.btn3_3.setText("12can")
        self.btn3_4.setText("6can")
        self.btn3_5.setText("24btl")
        self.btn3_6.setText("12btl")
        self.btn3_7.setText("6btl")
        self.btn3_8.setText("15can")
        self.btn3_9.setText("1TB")

    # premake cocktail amount menu show in 4th menu
    def show_premake_cocktail_amount(self):
        self.set_btnlist4_visible(7)

        self.btn4_1.setText("24")
        self.btn4_2.setText("18")
        self.btn4_3.setText("12")
        self.btn4_4.setText("6")
        self.btn4_5.setText("1")
        self.btn4_6.setVisible(False)
        self.btn4_7.setText("1TB")

    def set_btnlist2_visible(self,num):
        for i in range(len(self.btnLis2)):
            if i < num:
                self.btnLis2[i].setVisible(True)
            else:
                self.btnLis2[i].setVisible(False)

    def set_btnlist3_visible(self,num):
        for i in range(len(self.btnLis3)):
            if i < num:
                self.btnLis3[i].setVisible(True)
            else:
                self.btnLis3[i].setVisible(False)

    def set_btnlist4_visible(self,num):
        for i in range(len(self.btnLis4)):
            if i < num:
                self.btnLis4[i].setVisible(True)
            else:
                self.btnLis4[i].setVisible(False)

    def clear_btnlist1_checked(self,num):
        for i in range(len(self.btnLis1)):
            if i == num:
                continue
            elif self.btnLis1[i].isChecked():
                self.btnLis1[i].toggle()

    def clear_btnlist2_checked(self,num):
        for i in range(len(self.btnLis2)):
            if i == num:
                continue
            elif self.btnLis2[i].isChecked():
                self.btnLis2[i].toggle()

    def clear_btnlist3_checked(self,num):
        for i in range(len(self.btnLis3)):
            if i == num:
                continue
            elif self.btnLis3[i].isChecked():
                self.btnLis3[i].toggle()

    def clear_btnlist4_checked(self,num):
        for i in range(len(self.btnLis4)):
            if i == num:
                continue
            elif self.btnLis4[i].isChecked():
                self.btnLis4[i].toggle()
    
    # show orders of receipt
    def show_receipt(self,receipt):
        #??????order??????
        self.clear_list_order()
        #????????????
        self.list_order.addItem("-----------------------------------\n????????????\n-----------------------------------")
        for order in receipt.orders:
            self.list_order.addItem(
                order.show_order())

    # receipt list on clicked
    def list_receiptClicked(self):
        #???????????????????????????
        index = self.list_receipt.currentRow()
        selected_receipt = self.receipt_unpay[index]
        self.show_receipt(selected_receipt)

    # update receipt in receipt list with receipt index
    def update_receipt(self,receipt_idx):
        self.list_receipt.item(receipt_idx).setText('----------------------------------\n'+self.receipt_unpay[receipt_idx].show_receipt_brif()+'\n----------------------------------')

    # order list on clicked
    def list_orderClicked(self):
        # when click on other order, nothing going to change
        # when delete current receipt btn clicked
        if self.list_order.currentRow() == 0:
            self.clear_list_order()
            # get the current receipt
            index = self.list_receipt.currentRow()
            # remove the receipt from path
            self.receipt_unpay[index].remove_receipt()
            # delete the receipt from receipt list
            self.receipt_unpay.pop(index)
            self.list_receipt.takeItem(index)
            

    # clear the order list
    def clear_list_order(self):
        count = self.list_order.count()
        for i in range(count):
            self.list_order.takeItem(0)

    # add order to the receipt and update both list
    def addOrder(self,order):
        if self.list_receipt.count() == 0:
                return
        receipt_idx = self.list_receipt.currentRow()
        current_receipt = self.receipt_unpay[receipt_idx]
        #??????order??????
        current_receipt.add_order(order)
        self.list_order.addItem(order.show_order())
        #??????receipt??????
        self.update_receipt(receipt_idx)

    # add fast food favour to receipt with input of favour
    def addFastFood(self,favour):
        #??????1
        if self.btn1_2.isChecked():
            if self.btn2_1.isChecked():
                self.addOrder(Order("?????????",10.99,comment = favour))
            elif self.btn2_2.isChecked():
                self.addOrder(Order("??????",6,comment = favour))
            elif self.btn2_3.isChecked():
                self.addOrder(Order("??????",13.6,comment = favour))
            elif self.btn2_4.isChecked():
                self.addOrder(Order("??????", 9.99,comment = favour))
            elif self.btn2_5.isChecked():
                self.addOrder(Order("??????",8,comment = favour))
            elif self.btn2_6.isChecked():
                self.addOrder(Order("?????????",8,comment = favour))
            elif self.btn2_7.isChecked():
                self.addOrder(Order("?????????",8,comment = favour))
            elif self.btn2_8.isChecked():
                self.addOrder(Order("??????",13.99,comment = favour))
            elif self.btn2_9.isChecked():
                self.addOrder(Order("????????????",11.99,comment = favour))
        #??????2
        elif self.btn1_3.isChecked():
            if self.btn2_1.isChecked():
                self.addOrder(Order("??????",11.99,comment = favour))
            elif self.btn2_2.isChecked():
                self.addOrder(Order("??????",13.5,comment = favour))
            elif self.btn2_3.isChecked():
                self.addOrder(Order("?????????",11.99,comment = favour))
            elif self.btn2_4.isChecked():
                self.addOrder(Order("?????????", 9.99,comment = favour))
            elif self.btn2_5.isChecked():
                self.addOrder(Order("??????2???",5,comment = favour))
            elif self.btn2_6.isChecked():
                self.addOrder(Order("??????5???",9,comment = favour))
            elif self.btn2_7.isChecked():
                self.addOrder(Order("??????1???",3,comment = favour))
            elif self.btn2_8.isChecked():
                self.addOrder(Order("??????4???",9,comment = favour))

    # add beer to order
    # NOT USING
    def addBeer(self,favour):
        if self.btn1_4.isChecked():
            if self.btn2_1.isChecked():
                self.addOrder(Order("Kokanee",10.99,comment = favour))
            elif self.btn2_2.isChecked():
                self.addOrder(Order("Bud Weiser",6,comment = favour))
            elif self.btn2_3.isChecked():
                self.addOrder(Order("Bud Light",13.6,comment = favour))
            elif self.btn2_4.isChecked():
                self.addOrder(Order("Pilsner", 9.99,comment = favour))
            elif self.btn2_5.isChecked():
                self.addOrder(Order("Canadian",8,comment = favour))
            elif self.btn2_6.isChecked():
                self.addOrder(Order("Bohemian",8,comment = favour))
            elif self.btn2_7.isChecked():
                self.addOrder(Order("Calgary",8,comment = favour))
            elif self.btn2_8.isChecked():
                self.addOrder(Order("?????????",13.99,comment = favour))
            elif self.btn2_9.isChecked():
                self.addOrder(Order("Other",11.99,comment = favour))
        return

                
if __name__ == "__main__":
    #????????????PyQt5???????????????QApplication?????????sys.argv?????????????????????????????????????????????????????????
    app = QApplication(sys.argv)
    #?????????
    myWin = MyMainForm()
    #????????????
    myWin.showFullScreen()
    #?????????????????????????????????
    myWin.show()
    #???????????????sys.exit?????????????????????????????????
    sys.exit(app.exec_())



    
