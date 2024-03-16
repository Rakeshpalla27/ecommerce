"""r=reading the Dataa
w=opens in writes mode and override te data or cfreates the unexisgting files
a=doesnt overrides the data 
r+=read write
w+=override the data
a+=doesnt overeride
file.close()"""

# file=open('geek.txt','r')
def write():
    import csv
    f=open("student.csv","w",newline="")
    a=csv.writer(f)
    a.writerow(["studentid","rollno","name","mobileno"])
    while(True):
        print("write data y/n")
        a=input()
        if a=="y":
            a=csv.writer(f)
            studentid=int(input("enter the studentid"))
            rollno=input("enter rollno")
            name=input("enter the name ")
            mobileno=input("enter mobile no")
            a.writerow([studentid,rollno,name,mobileno])
            print("record has been saved")
        
            break
        elif a=="n":
            f.close()
            break
        else:
            print("enter a valid option")

def check():
    import csv
    with open('student.csv','r',newline="") as file:
        read=csv.DictReader(file)
        for row in read:
            print(row)
            return True
        return False
write()
check()
    
# import csv
# f=open("std.csv","a",newline="")
# a=csv.writer(f)
# a.writerow(["hello","hey"])
# hello=input("enter hello:")
# hey=input("enter hey")
# a.writerow([hello,hey])
# print("succesfully executed ")
# f.close()