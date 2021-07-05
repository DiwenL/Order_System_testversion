import os
import time
from Receipt import Receipt
from Order import Order

receipts = []

## menu init
menu = [0]
with open("menu.txt",encoding = 'utf-8') as f:
    menu_list = f.readlines()

for food in menu_list:
    fd = food.split(",")
    name = fd[0]+"\n"+fd[1]
    price = float(fd[2].split("\n")[0])
    menu.append(Order(name,price))


## UI init
def main_menu():
    print("Main Menu 主菜单")
    print("1. Check Receipts 现有单据")
    print("2. New Receipt    新建单据")
    
    flag = input("输入数字1或2,并回车")
    return flag

def receipts_menu():
    if len(receipts) == 0:
        print("Empty")
        time.sleep(5)
        return -1
    else:
        for receipt in receipts:
            receipt.show_receipt
        while 1:
            flag = input("enter the num to check the receipt\n输入单号并回车查看")
            try:
                receiptNum = int(flag)
            except:
                print("pleass enter receipt num\n请输入数字单号")
            else:
                if 0 < receiptNum and receiptNum < (len(receipts)+1):
                    return receiptNum
                else:
                    print("num out of range\n单号超出范围")
                    
    return flag        

def creat_receipt():
    receipt = Receipt()
    
    while True:
        os.system('cls')
        print("creating new receipt\n创建新单据")
        receipt.show_receipt_detail()

        print("0. return         返回")
        print("1. add order      添加内容")
        print("2. modify order   修改菜品")
        print("3. add phone      修改手机号")
        print("4. pickup time    修改取餐时间")
        print("5. paid stat      修改付款状态")
        print("6. print receipt  打印单据")

        flag = input()

        '''add order'''
        if flag == "1":
            while True:
                os.system("cls")
                print("0. return       返回")
                print("1. Soup         汤")
                print("2. Fried Rice   炒饭")
                print("3. Lo Mein      捞面")
                print("4. Chow Mein    炒面")
                print("5. Chop Sue     杂碎")
                print("6. Chef Special 厨师推荐")
                print("7. Combos       套餐")
                print("8. Special menu 特殊菜单")

                flag = input()

                if flag == "0":
                    break
                
                if flag == "1":
                    while True:
                        os.system("cls")
                        print("0. return       返回")
                        print("1. WontonSoup   云吞汤")
                        print("2. Wor Wonton   窝云吞")

                        flag = input()

                        try:
                            flag = int(flag)
                        except:
                            continue
                        else:
                            if flag == 0:
                                break
                            elif 0<flag<3:
                                receipt.add_order(menu[flag])
                                break
                            else:
                                continue
                    break


                if flag == "2":
                    while True:
                        os.system("cls")
                        print("0. return               返回")
                        print("1. Chicken Fried Rice   鸡炒饭")
                        print("2. Beef Fried Rice      牛炒饭")
                        print("3. Shrimp Fried Rice    虾炒饭")
                        print("4. Pork Fried Rice      猪炒饭")
                        print("5. Special Fried Rice   特殊炒饭")

                        flag = input()

                        try:
                            flag = int(flag)
                        except:
                            continue
                        else:
                            if flag == 0:
                                break
                            if 0<flag<6:
                                receipt.add_order(menu[flag+2])
                                break
                            else:
                                continue
                    break

                if flag == "3":
                    while True:
                        os.system("cls")
                        print("0. return            返回")
                        print("1. Chicken Lo Mein   鸡捞面")
                        print("2. Beef Lo Mein      牛捞面")
                        print("3. Shrimp Lo Mein    虾捞面")
                        print("4. Pork Lo Mein      猪捞面")
                        print("5. Special Lo Mein   特殊捞面")

                        flag = input()

                        try:
                            flag = int(flag)
                        except:
                            continue
                        else:
                            if flag == 0:
                                break
                            if 0<flag<6:
                                receipt.add_order(menu[flag+7])
                                break
                            else:
                                continue

                    break

                if flag == "4":
                    while True:
                        os.system("cls")
                        print("0. return              返回")
                        print("1. Chicken Chow Mein   鸡炒面")
                        print("2. Beef Chow Mein      牛炒面")
                        print("3. Shrimp Chow Mein    虾炒面")
                        print("4. Pork Chow Mein      猪炒面")
                        print("5. Special Chow Mein   特殊炒面")

                        flag = input()

                        try:
                            flag = int(flag)
                        except:
                            continue
                        else:
                            if flag == 0:
                                break
                            if 0<flag<6:
                                receipt.add_order(menu[flag+12])
                                break
                            else:
                                continue
                    break

                if flag == "5":
                    while True:
                        os.system("cls")
                        print("0. return              返回")
                        print("1. Chicken Chop Suey   鸡杂碎")
                        print("2. Beef Chop Suey      牛杂碎")
                        print("3. Shrimp Chop Suey    虾杂碎")
                        print("4. Pork Chop Suey      猪杂碎")
                        print("5. Special Chop Suey   特殊杂碎")

                        flag = input()

                        try:
                            flag = int(flag)
                        except:
                            continue
                        else:
                            if flag == 0:
                                break
                            if 0<flag<6:
                                receipt.add_order(menu[flag+17])
                                break
                            else:
                                continue
                    break

                if flag == "6":
                    while True:
                        os.system('cls')
                        print("0. return                     返回")
                        print("1. Beef with Broccoli         牛肉西兰花")
                        print("2. Beef Vegetables            牛杂菜")
                        print("3. Chicken Vegetables         鸡杂菜")
                        print("4. Ginger Beef                姜炒牛肉")
                        print("5. Shanghai Noodle            上海面")
                        print("6. Singpore Noodle            新加坡面")
                        print("7. Sweet & Sour Pork          酸甜猪肉")
                        print("8. Sweet & Sour Chicken       酸甜鸡肉")
                        print("9. Vegetables                 蔬菜")
                        print("10. Sichuan beef              四川牛肉")
                        print("11. Sichuan Pork              四川猪肉")
                        print("12. Chicken Shredded with Pepper 鸡丝炒椒")
                        print("13. Hot Pot Beef              牛肉火锅")

                        flag = input()

                        try:
                            flag = int(flag)
                        except:
                            continue
                        else:
                            if flag == 0:
                                break
                            if 0<flag<14:
                                receipt.add_order(menu[flag+22])
                                break
                            else:
                                continue
                    break

                if flag == "7":
                    while True:
                        os.system('cls')
                        print("0. return      返回")
                        print("1. Combo A     A餐")
                        print("2. Combo B     B餐")
                        print("3. Combo C     C餐")
                        print("4. Combo D     D餐")
                        print("5. Combo 2     二人餐")
                        print("6. Combo 3     三人餐")
                        print("7. Combo 4     四人餐")
                        print("8. Combo 5     五人餐")
                        print("9. Combo 6     六人餐")
                        print("10.Combo 8     八人餐")

                        flag = input()

                        try:
                            flag = int(flag)
                        except:
                            continue
                        else:
                            if flag == 0:
                                break
                            if 0<flag<10:
                                receipt.add_order(menu[flag+35])
                                break
                            else:
                                continue
                    break


                if flag == "8":
                    favourLis = ["sweet & sour\n      酸甜","salt & pepper\n      椒盐","buffalo","hot\n      辣酱","ranch","sweet chill\n      甜辣酱","honey garlie\n      蜂蜜","lemon pepper\n      柠檬辣椒","greek","black label\n      柠檬水辣酱","seasoning salt\n      调味盐","BBQ\n      烧烤酱","teriyaki"]
                    while True:
                        os.system('cls')
                        print("0. return                    返回")
                        print("1. Deef Fried Wonton         炸云吞")
                        print("2. Crispy Coated Frieds      炸薯条")
                        print("3. Chicken Tender            鸡块")
                        print("4. Chicken Wings             鸡翼")
                        print("5. Poutine                   肉酱薯条")
                        print("6. Mozzarella Stick          芝士条")
                        print("7. Fired Onion Rings         炸洋葱圈")
                        print("8. Fired Dumpling            煎饺")
                        print("9. Chicken Tender with Fries 鸡块薯条")
                        print("10.Chicken Balls             鸡球")
                        print("11.Deef Fried Shrimp         炸虾")
                        print("12.Deef Fried Ribs           炸排骨")
                        print("13.Chinese Cabbage Fritter   白菜卷")
                        print("14.Egg Roll 2pc              蛋卷2个")
                        print("15.Egg Roll 5pc              蛋卷5个")
                        print("16.Spring Roll 1pc           春卷1个")
                        print("17.Spring Roll 4pc           春卷4个")

                        flag = input()

                        try:
                            flag = int(flag)
                        except:
                            continue
                        else:
                            if flag == 0:
                                break
                            if 0<flag<18:
                                order = menu[flag+45]
                                while True:
                                    os.system('cls')
                                    i = 0
                                    print("0. no favour 不要酱")
                                    for favour in favourLis:
                                        i+=1
                                        print(str(i)+". "+favourLis[i-1])
                                    try:
                                        chose = int(input())
                                    except:
                                        continue
                                    else:
                                        if chose == 0:
                                            break
                                        else:
                                            order.add_comment(favourLis[chose-1])
                                            break
                                receipt.add_order(order)
                                break
                            else:
                                continue
                    break

        '''modify order'''
        if flag == "2":
            if receipt.orders == []:
                continue
            else:
                '''show orders'''
                while True:
                    os.system('cls')
                    print("0. return 返回")
                    for i in range(len(receipt.orders)):
                        print(str(i+1) + ". ",end='')
                        receipt.orders[i].show_order()

                    select = input()
                    try:
                        select = int(select)
                    except:
                        continue
                    
                    if select == 0:
                        break
                    elif 0<select<len(receipt.orders)+1:
                        '''order selected'''
                        select -= 1
                        while True:
                            os.system('cls')
                            print("0. return         返回")
                            print("1. modify amount  修改数量")
                            print("2. modify cost    修改价格")
                            print("3. delect order   删除")

                            flag = input()

                            try:
                                flag = int(flag)
                            except:
                                continue

                            if flag == 0:
                                break
                            if flag == 1:
                                amount = input("new amount 修改数量为:")
                                try:
                                    amount = int(amount)
                                except:
                                    continue
                                receipt.orders[select].set_amount(amount)
                                break
                            if flag == 2:
                                price = input("new price 修改价格为:")
                                try:
                                    price = int(price)
                                except:
                                    continue
                                receipt.orders[select].set_total_cost(price)
                                break
                            if flag == 3:
                                receipt.delete_order(select)
                                break
                        break

        '''phone'''
        if flag == "3":
            phoneNum = input("\phone number 输入手机号:")
            receipt.set_phone(phoneNum)

        '''pickup time'''
        if flag == "4":
            pickup = input("pick up @ 几点取餐 :")
            receipt.set_pickup(pickup)
            
        '''pay stat'''
        if flag == "5":
            while True:
                os.system('cls')
                print("0. return  返回")
                print("1. cash    现金")
                print("2. card    刷卡")
                print("3. emt     邮箱")
                pay = input()
                if pay == "0":
                    break
                elif pay == "1":
                    receipt.paystat = "Cash 现金"
                    break
                elif pay == "2":
                    invoiceNum = input("invoice number 单号:")
                    receipt.paystat = "Card 刷卡  #" + invoiceNum
                    break
                elif pay == "3":
                    receipt.paystat = "Emt 邮箱转账"
                    break

        '''print receipt'''
        if flag == "6":
            print("printing the receipt\n正在打印单据")
            receipt.print_receipt()
            time.sleep(3)
            print("receipt printed\n已打印")
            time.sleep(1.5)

    
    
def main():
    while True:
        creat_receipt()


main()
