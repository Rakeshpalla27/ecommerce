import csv
import orders as od
ob1=od.order()
class stock:
    def sto(self):
        with open('stock.csv','r',newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                print(row)
        print("enter the PRODUCT NAME that you want to order:")
        while(True):
            a=input()
            if a=="ledlight":
                print("stock availablle")
                with open('stock.csv','r',newline="") as file:
                    read=csv.DictReader(file)
                    for row in read:
                        print(row['ledlight'])
                print("price of the ledlight : 230")
                print("do you want to place an order y/n:")
                x=input()
                if x=="y":
                    ob1.ord(a)
                else:
                    break
            elif a=="smartwatch":
                print("stock availablle")
                with open('stock.csv','r',newline="") as file:
                    read=csv.DictReader(file)
                    for row in read:
                        print(row['smartwatch'])
                print("price of the smartwatch : 330")
                print("do you want to place an order y/n:")
                x=input()
                if x=="y":
                    ob1.ord(a)
                else:
                    break
            elif a=="nailpolish":
                print("stock available")
                with open('stock.csv','r',newline="") as file:
                    read=csv.DictReader(file)
                    for row in read:
                        print(row['nailpolish'])
                print("price of the smartwatch : 30")
                print("do you want to place an order y/n:")
                x=input()
                if x=="y":
                    ob1.ord(a)
                else:
                    break
            elif a=="wintercoat":
                print("stock availablle")
                with open('stock.csv','r',newline="") as file:
                    read=csv.DictReader(file)
                    for row in read:
                        print(row['wintercoat'])
                print("price of the smartwatch : 530")
                print("do you want to place an order y/n:")
                x=input()
                if x=="y":
                    ob1.ord(a)
                else:
                    break
            elif a=="blueshoe":
                print("stock availablle")
                with open('stock.csv','r',newline="") as file:
                    read=csv.DictReader(file)
                    for row in read:
                        print(row['blueshoe'])

                print("price of the smartwatch : 900")
                print("do you want to place an order y/n:")
                x=input()
                if x=="y":
                    ob1.ord(a)
                else:
                    break
            else:
                print("enter the valid product name")
        

