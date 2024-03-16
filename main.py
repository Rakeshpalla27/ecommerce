
"""create an eccomeerce project where the user can registor and login him self
 he can see what all the products are present the productss contain name,price,category,and stock left
 from these products user can place an order just by the product name and the quantity he want to purchase
 once he enters this a bill should should be generated with the total amount and a msg should be given order has been placed
 complete the payment of the delevery
 the change of shock should be reflected on the list of products """
import csv
import regiorlog as re
re1=re.ral()
print("#WELCOME TO THE ECOMMERCE SITE ")
with open('data.csv','w',newline="") as f:
    a=csv.writer(f)
    a.writerow(["username","password","orders","mobileno"])
print()
while(True):
    print("1.registor  2.login 3.exit")
    a=input("enter number or type name:")
    if a=='1' or a=='register':
        
            re1.registor()
            print("Now you need to #LOGIN ")
            re1.login()
    elif a=='2' or a=='login':
        re1.login()
        break 
    elif a=='3' or a=='exit':
         break
    else:
        print("enter a valid option")
        continue