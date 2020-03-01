#Eס 1 - sulotion1:
num=4567
print("\nAlafim:"+str(int(num/1000)) + "\nMeot:"+str(int((num%1000)/100)) + "\nAsarot:"+str((int(((num%1000)%100)/10))) + "\nAhadot"+str(int((((num%1000)%100)%10))))

#Excersie 1 - sulotion2 with loop:
n=input("\nplease enter number")
n=int(n)
while n > 0 :
    print (n%10)
    n = int(n/10)

#Excersie 2 - sulotion:
print("Welcome to Rami Levy")
var1=input("please enter how manny tomattows")
var2=input("please enter how manny cuecumbers")
var3=input("please enter how manny colas")
var4=input("please enter how much chicken (kg)")

total=(float(var1)*3+float(var2)*2+float(var3)*5+float(var4)*20)*1.17
print("tottal payment:" + str(round(total,2)))

#Excersie 3 - Pet shop - sulotion:
dog1=int(input("Please enter how manny Pincher you wish to purcehs:"))
age1=int(input("Please enter their ages:"))
dog2=int(input("Please enter how manny Rotvilers you wish to purcehs:"))
age2=int(input("Please enter their ages:"))
dog3=int(input("Please enter how manny Aski you wish to purcehs:"))
age3=int(input("Please enter their ages:"))

tottalPrice=dog1*100+dog2*200+dog3*300
tottalDogs=dog1+dog2+dog3
avg=((dog1*age1+dog2*age2+dog3*age3)/tottalDogs)*7
print("Tottal Price: " + str(tottalPrice) + "\nTottal amount of dogs purchesed: " + str(tottalDogs) + "\nAvrage Dpgs age in human years: "+str(avg))

#Excersie 4 - sulotion:
Ger=float(input("please enter months of rented appartment Germany"))
Isr=float(input("please enter months of rented appartment Israel"))
Coins=float(input("please enter how many coins you have"))
euro=3.88
usd=3.45
print ("Tottal income:"+str(Ger*euro*500+Coins*usd*2+Isr*3000)+" shmekels")

#Excersie 5 - sulotion:
dog_list=["pug","husky","buldog","hushpuppy","rotwiler"]
print( input ("please enter dog type: " ) in dog_list)

#Excersie 6 - sulotion:
my_list=[]
my_list.append(input("please enter first IP address: "))
my_list.append(input("please enter 2nd IP address: "))
my_list.append(input("please enter 3rd IP address: "))
my_list.append(input("please enter 4th IP address: "))
my_list.append(input("please enter 5th IP address: "))
var=input("please new IP to check: ")
if var in my_list:
    print ("this ip is not avilable!")
else:
    my_list.append(var)
    print("New Ip was added to the list!")

#Excersie 7: Cassino - sulotion:
from time import sleep
import random

print ("\n Welcome to the CAZINO!!")
cube1=random.randrange(1,6,1)
cube2=random.randrange(1,6,1)
print ("\nRolling dice...")
if cube1 == cube2 :
    if cube1 == 6:
        print("you won 1000$!!!")
    else:
        print("you won 100$!")
elif cube2==2:
    print("You won 15$!")
elif cube1==1:
    print("You won 5$!")
else:
    print("Sorry, you didnt won this time..")
sleep (5)
print("\nThanks for playing , see you next time.")

#Excersie 8: Random - sulotion:
import random
choise = input('''
Menu:
1) Enter two numbers to add.
2) Roll 2 Dices.
3) Show my details.
4) Insert Ip address to list.
''')
if choise == "1":
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    print("Result: " + str(num1+num2))
elif choise == "2":
    print("First Dice: " + str(random.randrange(1, 6, 1)) + "\nSecond  Dice: " + str(random.randrange(1,6,1)))
elif choise == "3":
    print("Name: Ori\nAge:36\nMail:Oris07@gmail.com")
elif choise == "4":
    my_list = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]
    var = input("please enter new IP : ")
    if var in my_list:
        print("this ip is not avilable!")
    else:
        my_list.append(var)
        print("New Ip was added to the list!")
    print("IP List: " + str(my_list))
else:
    print("\nPlease chose 1-4.")

#Excersie 9: Dictionary - sulotion:
dict = {}
i=0
err=0
while i < 2:
    key=input("please enter name: ")
    if key in dict:
        print("Error")
        err=err+1
    else:
        phone = input("please enter phone: ")
        if phone in dict.values():
            print("Please change your phone in the next two days.")
        dict.update({key: phone})
        # dict[key] = phone
    i=i+1
print("tottal people: " + str(len(dict)))
print("tottal errors: " + str(err))



#Excersie 10: Sulotion in  Exercise_DNS(10,14) Directory.

#Excersie 11:  sulotions in Beginner.Exercises_11 Directory.

#Excersie 12:  - sulotion:
import random
num1=str(random.randrange(1, 101, 1))
count=0
while 1:
    num2=input("Please enter a number: ")
    count=count+1
    if num1== num2:
        print("You hit the correct number: " + num1 + "\nIt took you: " + str(count) + " tries")
        break
    else:
        print("try again!")

#Excersie 13: My sulotion - Lottery :
import random
win_list = []
for i in range(6):
    win_list.append(str(random.randrange(1,38,1)))

credits=int(input("Please enter credit: "))
rows = []
while credits > 2:
    new_row = []
    for j in range(6):
        new_row.append(input("Please enter a number between 1 to 37: "))
    rows.append(new_row)
    credits = credits - 3
print(rows)
print(len(rows))
prize = 0
for i in range (len(rows)):
    counter = 0
    for j in range(6):
        if (rows[i])[j] in win_list:
            counter=counter+1
    if counter == 6:
        prize=prize+1000000
    elif counter == 5:
        prize=prize+5000
    elif counter == 4:
        prize=prize+250
    elif counter == 3:
        prize=prize+10
print(prize)

#Excersie 13: Class sulotion - Lottery:
import random
customer=[]
Money=int(input("Enter how many shekels you have: "))
for i in range(int(Money/3)):
    print("Please print your 6 numbers in a row: ")
    string=[]
    for j in range(6):
        num=int(input("Enter a number: "))
        while num<1 or num>37 or num in string:
            print ("Enter 1-37 only or stop duplicate!")
            num = int(input("Enter a number: "))
        string.append(num)
    customer.append(string)
print(customer)
print(len(customer))

#Excersie 14: Sulotion in Exercise_DNS(10,14) Directory.

#Excersie 15: Lottery - sulotion in Beginner.Exercise_15_Lottery Directory

#Excersie 16:  - sulotion:
def check_name (filename,name):
    file=open(filename,'r')
    for line in file:
        if name in line:
            print(name+" exists in file. ")
            file.close()
            return (1)
    print(name + " doesnt exists in file. ")
    file.close()
    return (0)

def enter_new (filename,name,age,phone):
    file=open(filename,'a')
    file.write(name+"\t"+age+"\t"+phone+"\n")
    file.close()
    return

filepath=r"c:\Exercises\users.txt"
file=open(filepath,'w')
file.write("Name:\tAge:\tPhone\n")
file.close()
for i in range(2):
    name = input("Enter name: ")
    while check_name(filepath,name) ==1:
        name = input("Enter name: ")
    age = input("Enter age: ")
    phone = input("Enter phone: ")
    enter_new(filepath,name,age,phone)

#Excersie 17:  - sulotion: ***********DOESNT WORK***********

filepath=r"c:\Exercises\IPs.txt"
file=open(filepath,"w")
file.write("IPs:\n")
while 1:
    ip=input("Please enter IP: ")
    file.write(ip + "\n")
    if input("exit?(yes/no)")=="yes":
        break
file.close()

iplist=[]
file=open(filepath,'r')
for line in file:
    iplist.append(line)
file.close()

new_ip=input("please enter new IP:")

if new_ip in iplist: #never enters!!!!!*** need to add splitlines.
    iplist.remove(new_ip)
    file = open(filepath, 'w')
    for i in range(len(iplist)):
        file.write(iplist[i])
    file.close()
else:
    file=open(filepath,'a')
    file.write(new_ip)
    file.close()

