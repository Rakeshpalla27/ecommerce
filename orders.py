import csv
class order:
    def ord(self,a):
        self.name=a
        b=int(input("enter the quantity needed:"))
        with open('stockss.csv','r',newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                x=int(row[self.name])-b
                print("The left over stocks is :")
                print(x)
                print("thanks for ordering we have placed an order for you")