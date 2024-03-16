# class faculty:
#     def __init__(self,f_name,dep,f_id):
#         self.fname=f_name
#         self.dep=dep
#         self.fid=f_id
#     def print_info(self):
#         print("faculty info",self.fname,self.dep,self.fid)
# ob=faculty("raki","cse",2003)
# ob.print_info()
# class cse(faculty):
#     pass
# ob1=cse("ramu","it",2204)
# ob1.print_info()
"""create a cls of name placements which has a function info which displays the no of placements  this year
663.create another cls name department with function display which displayds the name of departments
present in the college,create a class pragati with a function welcome which displays the msg  welocme and this 
pragati cls show also display the details about departments and placements """
# class placements:
#     def place24(self):
#         print()
#         print("TOTAL NO OF PLCAEMENTS IN THE YEAR OF 2024")
        
#         print("650+ and stilll counting")

# class department:
#     def departments(self):
#         print()
#         print("DEPARTMENTS AVALABLE:")
#         print("1.cse",end="")
#         print("2.ece",end="")
#         print("3.mech",end="")
#         print("4.eee",end="")
#         print()
    
# class pragati(department,placements):
#     def __init__(self):
#         print()
#         print("WELCOME TO THE PRAGATI ENGINEERING COLLEGE")
#         print("WE ARE GLAD THAT YOUR HERE CHECK OF THE DETAILS")
# ob=pragati()
# ob.departments()
# ob.place24()

# class name():
#     def nam(self):
#         print("name is raki")
# class age():
#     def age(self):
#         print("my age is 21")
# class dob(age,name):
#     def db(self):
#         print("my dob is 2003")
# ob=dob()
# ob.nam()
# ob.age()
# ob.db()
"""function overloading (compiler polymorphism) same function name but different fucntionality """
# class arth:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):   """doesnt support compile tym polymorphism-last fucntion is executed"""
#         print(a+b+c)
# obj=arth()
# obj.add(1)
# obj.add(1,2)
# obj.add(1,2,3)
"""fucntion ,constructor doesnt support compile tym polymorphism only operator ovverloading works"""


"""runtym ploymerphism (changing the decision of grandfather land ,father plan land ,and me form house
OVERRIDIGNG IS POSSSIBLE FUNCTION AND COONSTRUCTOR) """
# class father():
#     def bike(self):
#         print("harley devidson")
#     def laptop(self):
#         print("2gb and basic configurations")
# class anji(father):
#     def laptop(self):
#         print("high advanced")
# pb=anji()
# pb.laptop()
# pb.bike()
"""create a cls ticket which will be abstract cls inside that create a fucntion "book ticket" which 
will be the abstract method and has ntg in it.create a cls MAKE MY  TRIP which will use the book ticket 
fucntion from ticket cls to take the details such as name ,phone no,email joourney date and display a msg 
saying tq for booking from make my trip.create a cls isrtc which will ust ethe book ticket same details of 
make my trip but in the end it will give the option to user to select whether it is one way or round trip
if user option is wrong trip it again asks the user to enter the return data is well and then prints
thank you irctc else it prints the choosing irctc .create a class indigo which takes all the details as irctc 
and just asks which mode of transport you want to go in train ,flight or bus and display tq for choosing 
indigo"""
# from abc import (ABC,abstractmethod)
# class ticket(ABC):
#     @abstractmethod
#     def  bookticket(self):
#         pass
        
# class makemytrip(ticket):
#     def bookticket(self):
#         print("WELCOME TO MAKEMYTRIP:")
#         print()
#         name=input("enter name:")
#         phone=int(input("enter phone no:"))
#         email=input("enter email:")
#         jour=input("enter the date for booking:")
#         print("THANK YOU FOR BOOKING THROUGH 'MAKE MY TRIP'")
# class irctc(ticket):
#     def bookticket(self):
#         print("WELCOME TO IRCTC:")
#         print()
#         name=input("enter name:")
#         phone=int(input("enter phone no:"))
#         email=input("enter email:")
#         jour=input("enter the date for booking:")
#         while(True):
#             print()
#             print("select the trip")
#             print("1.onewaytrip",end=" ")
#             print("2.roundway",end=" ")
#             print()
#             b=input()
#             if b=="1" or b=="onewaytrip" or b=='2' or b=="roundway" :
#                 print("THANK YOU FOR BOOKING IN IRCTC")
#                 break
#             else:
#                 print("enter way is invalid select the correct way")
                
       

# class indigo(ticket):
#     def bookticket(self):
#         print("WELCOME TO INDIGO")
#         print()
#         name=input("enter name:")
#         phone=int(input("enter phone no:"))
#         email=input("enter email:")
#         jour=input("enter the date for booking:")
#         while(True):
#             print()
#             print("select the trip")
#             print("1.onewaytrip",end=" ")
#             print("2.roundway",end=" ")
#             print()
#             b=input()
#             if b=="1" or b=="onewaytrip" or b=='2' or b=="roundway" :
#                 print("THANK YOU FOR BOOKING IN IRCTC")
#                 break
#             else:
#                 print("enter way is invalid select the correct way")
#         while(True):
#             print()
#             print("mode of transport")
#             print("1.flight",end=" ")
#             print("2.bus",end=" ")
#             print("3.train",end=" ")
#             print()
#             b=input()
#             if b=="1" or b=="flight" or b=='2' or b=="bus" or b=='3' or b=="train":
#                 print("THANK YOU FOR BOOKING IN indigo")
#                 break
#             else:
#                 print("enter mode of transportation is invialid select the correct way ")

# print("WELCOME TO TICKET BOOKING SITE:")
# print()
# print("available booking sites")
# print("1.makemytrip",end=" ")
# print("2.irctc",end=" ")
# print("3.indigo",end=" ")
# print()
# a=input()
# if a=='1' or a=="makemytrip":
#     ob=makemytrip()
#     ob.bookticket()
# elif a=='2' or a=="irctc":
#     ob=irctc()
#     ob.bookticket()
# elif a=='3' or a=="indigo":
#     ob=indigo()
#     ob.bookticket()
# else:
#     print("sry we doesnt contain the enterd site")








