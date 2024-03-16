# class raki:
#     b=10
#     def a(self):
#         print("hello")
# ob=raki()
# ob.a()
# print(ob.b)
"""create a class f15 with functions lights,fans,and ac 
when lights called prints-color of the light 
when fan called it displays the speed in which it is rotationing when it is taken as the parameter funcion
when ac called it dis room temp and outside which are taken as parameters 
display which displays the difference in outside and room temp"""
# class f15:
#     light=12
#     def __init__(self,nigga):
#         print(f'pavan is {nigga}')
#         print("helo i am constructor")
#         a=9
#         b=90
#         print(b-a)
#     def lights(mova,color):
#         print(f'color of the light {color}')
#     def fan(mova,speed):
#         print(f'speed of the fan {speed}')
#     def ac(mova,room,out):
#         mova.room=room
#         mova.out1=out
#         print(f'room temp {room} and outside temp {out}')
#     def display(mova):
#         print(f'differnce {mova.out1-mova.room}')


# ob=f15("nigga")
# ob.lights("blue")
# ob.fan(45)
# ob.ac(25,45)
# ob.display()
# print(ob.light)
"""input form user for the car model name for the car company name and in the input msg give the user the 
3 options of the cmpies ,this campy name goes as the input/arguement to model name function ,which 
welcomes the user accordingly to the compay name ask the user to enter the specific model name for that cmpy  ,the second fucntion nmae 
"variant " according to the car cmpy name and car model the user should be asked to enter the variant 
would you like to choose from petrol ,desel .the last function display according to car cmpy ,model 
variant first its ex showroom price will be dispayed and then its on road pirce should be displayed which is 
calcu lated as ex showroom price +cgst+sgst+insurance. the sgst,cgst and the insurance all the three 
have common value throught the car showroom """
class car:
    sgst=10
    cgst=20
    insu=20
    def display(self,mdl,var):
        if mdl=="moto300"  and var=="petrol":
            price=510000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy in percentage={self.sgst}')
            print(f'cgst fo the compy in percentage={self.cgst}')
            print(f'insu fo the compy percentage={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="moto300"  and var=="desel":
            price=540000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="moto600"  and var=="petrol":
            price=770000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="moto600"  and var=="desel":
            price=630000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="moto900"  and var=="petrol":
            price=800000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="moto900"  and var=="desel":
            price=750000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="mercitle300"  and var=="petrol":
            price=300000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="mercitle300"  and var=="desel":
            price=450000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="mercitle600"  and var=="petrol":
            price=550000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="mercitle600"  and var=="desel":
            price=500000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="mercitle900"  and var=="petrol":
            price=800000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="mercitle900"  and var=="desel":
            price=900000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="sonota300"  and var=="petrol":
            price=350000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="sonota300"  and var=="desel":
            price=400000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="sonota600"  and var=="petrol":
            price=700000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="sonota600"  and var=="desel":
            price=600000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="sonota900"  and var=="petrol":
            price=900000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)
        if mdl=="sonota900"  and var=="desel":
            price=800000
            print("PRICE BILL IF YOU WANT TO BUY:")
            print()
            print(f'sgst fo the compy={self.sgst}')
            print(f'cgst fo the compy={self.cgst}')
            print(f'insu fo the compy={self.insu}')
            print("after calculations the total price of the car:")
            price=price*self.sgst+self.sgst+self.insu/10
            print()
            print(price)

            

def model(mdl):
    if mdl=="moto300":
        print()
        print(f'enter car model was {mdl}')
        print("avaiable variants in the model:")
        print("1.petrol",end=" ")
        print("2.desel")
        print()
        var=input("enter the 'VARIANT TYPE' you want to see:")
        ob.display(mdl,var)
    elif mdl=="moto600":
        print()
        print(f'enter car model was {mdl}')
        print("avaiable variants in the model:")
        print("1.petrol",end=" ")
        print("2.desel")
        print()
        var=input("enter the 'VARIANT TYPE' you want to see:")
        ob.display(mdl,var)
    if mdl=="moto900":
        print()
        print(f'enter car model was {mdl}')
        print("avaiable variants in the model:")
        print("1.petrol",end=" ")
        print("2.desel")
        print()
        var=input("enter the 'VARIANT TYPE' you want to see:")
        ob.display(mdl,var)
    if mdl=="mercitle300":
        print()
        print(f'enter car model was {mdl}')
        print("avaiable variants in the model:")
        print("1.petrol",end=" ")
        print("2.desel")
        print()
        var=input("enter the 'VARIANT TYPE' you want to see:")
        ob.display(mdl,var)
    if mdl=="mercitle600":
        print()
        print(f'enter car model was {mdl}')
        print("avaiable variants in the model:")
        print("1.petrol",end=" ")
        print("2.desel")
        print()
        var=input("enter the 'VARIANT TYPE' you want to see:")
        ob.display(mdl,var)
    if mdl=="mercitle900":
        print()
        print(f'enter car model was {mdl}')
        print("avaiable variants in the model:")
        print("1.petrol",end=" ")
        print("2.desel")
        print()
        var=input("enter the 'VARIANT TYPE' you want to see:")
        ob.display(mdl,var)
    if mdl=="sonota300":
        print()
        print(f'enter car model was {mdl}')
        print("avaiable variants in the model:")
        print("1.petrol",end=" ")
        print("2.desel")
        print()
        var=input("enter the 'VARIANT TYPE' you want to see:")
        ob.display(mdl,var)
    if mdl=="sonota600":
        print()
        print(f'enter car model was {mdl}')
        print("avaiable variants in the model:")
        print("1.petrol",end=" ")
        print("2.desel")
        print()
        var=input("enter the 'VARIANT TYPE' you want to see:")
        ob.display(mdl,var)
    if mdl=="sonota900":
        print()
        print(f'enter car model was {mdl}')
        print("avaiable variants in the model:")
        print("1.petrol",end=" ")
        print("2.desel")
        print()
        var=input("enter the 'VARIANT TYPE' you want to see:")
        ob.display(mdl,var)
        
def com(cmpy):
    if cmpy=="moto":
        print("\n")
        print("#WELCOME TO THE MOTO")
        print()
        print("avaible model of this company is :")
        print("1.moto300",end=" ")
        print("2.moto600",end=" ")
        print("3.moto900")
        print()
        mdl=input("enter the 'MODEL NAME' u want to buy:")
        model(mdl)
        
    elif cmpy=="mercitle":
        print("\n")
        print("#WELCOME TO THE MERCITLE")
        print()
        print("avaible model of this company is :")
        print("1.mercitle300",end=" ")
        print("2.mercitle600",end=" ")
        print("3.mercitle900")
        print()
        mdl=input("enter the 'MODEL NAME' u want to buy:")
        model(mdl)
    elif cmpy=="sonota":
        print("\n")
        print("#WELCOME TO THE SONOTA")
        print()
        print("avaible model of this company is :")
        print("1.sonota",end=" ")
        print("2.sonota",end=" ")
        print("3.sonota900")
        print()
        mdl=input("enter the 'MODEL NAME' u want to buy:")
        model(mdl)
    else:
        print("sry sir we doesnt have such company in our showroom")

print("WELCOME TO THE #KAUSKIK SHOWROOM#:")
print()
ob=car()
print("companies of the cars available in our showroom")
print("1.moto",end=" ")
print("2.mercitles",end=" ")
print("3.sonota")
print()
cmpy=input("enter the 'COMPANY NAME' you want to see:")
com(cmpy)

