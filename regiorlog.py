import csv
import stocks as st
st1=st.stock()
class ral:
    def registor(self):
        with open('data.csv','a',newline="") as f:
            a=csv.writer(f)
            print()
            print("#enter your data for #REGISTRATION:")
            print()
            username=input("enter username:")
            password=input("create password :")
            orders=0
            mobileno=input("enter mobile no")
            a.writerow([username,password,orders,mobileno])
            print()
            print("You have #REGISTERED SUCCESSFULLY")
            print()
            
    def login(self):
        with open('data.csv','r',newline="") as f:
            read=csv.DictReader(f)
            print("login with your credentials")
            print()
            username=input("enter the name:")
            password=input("enter password")
            for row in read:
                if row['username']==username and row['password']==password:
                    print()
                    print("successfull login")
                    with open('stock.csv','a',newline="") as f:
                        a=csv.writer(f)
                        a.writerow(["ledlight","smartwatch","nailpolish","wintercoat","blueshoe"])
                        a.writerow([23,11,45,67,78])
                        st1.sto()
                    
                else:
                    print("incorrect credentials")
                    break
        


