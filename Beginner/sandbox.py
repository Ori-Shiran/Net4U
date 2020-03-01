# var1=1
# print ("1\t2")
# print (''' Hello world
# Hello world 2
# Hello world 3
# ''')
# # print ("idan" in input("Enter your email: "))
# a="idan"
# print(a[0:3])
# my_list=[1,69.72,"Ori Shiran"]
# print(type(my_list))
# print("My list is:"+ str(my_list))
# print(len(my_list))
# my_list=["ori shiran","054323323","ori@gmail.com",20.3]
# print("my name: " + my_list[0])
# print("my phone: " + my_list[1])
# print("my mail: " + my_list[2])
# print("my age: " + str(my_list[3]))
# my_list=["ori shiran","054323323","ori@gmail.com",20.3,[45,48.6,"66"]]
# print((my_list[4])[1])

## family=[["Ori Shiran",30,"054334434"],["liad Shiran",32,"0532324434"],["Ran Shiran",34,"05432434"],["Malka Shiran",40,"0532432434"],]
# print((family[3])[1])
# my_list=[11,22,33]
# my_list=my_list+[77]
# print (my_list)
# my_list=list("123456789")
# print(my_list)
#
# var="dsadsa"
# print(var[2])

# my_list=["11","22","33","44"]
# my_list.append("hello")
# print(my_list)
#
# my_list=[]
# my_list.append(input("please enter first IP address: "))
# my_list.append(input("please enter 2nd IP address: "))
# my_list.append(input("please enter 3rd IP address: "))
# my_list.append(input("please enter 4th IP address: "))
# my_list.append(input("please enter 5th IP address: "))
# var=input("please new IP to check: ")
# if var in my_list:
#     print ("this ip is not avilable!")
# else:
#     my_list.append(var)
#     print("New Ip was added to the list!")
# print("IP List: " + str(my_list))
# if not 9:
#     pass
# else:
#     raise Exception('bad')
#
# name="ori"
# index=1
# print(name[index])
# my_dict1={}
# my_dict2=dict()
# my_dict3={'int' : 0, 'float' : 1.0 , 'str' : '3' , 'list' : []}
# my_dict4=dict(ani='optimus',idan='prime')
# # my_dict5=dict(my_dict3, **)
# print(my_dict1)
# print(my_dict2)
# print(my_dict3)
# print(my_dict4)


# for i in range (1,6):
#     print(i)
#
# def hello_world():
#     print("Hello world")
#
# def tax ():
#     return(float(1.17))
#
#
# def add_2_numbers(num1,num2):
#     return(int(num1*num2))
#
# hello_world()
#
# print(tax())
#
# print(add_2_numbers(4,2))
#
# file handling:
# def details(filename):
#     name=input("please enter name")
#     name=checkname(name, filename)
#     age=input("please enter age")
#     phone=input("please enter phone")
#     file=open(filename, "a")
#     file.write(name + ", " + age + ", " + phone+"\n")
#     file.close()
#
# def checkname(name, filename):
#     new_name=name
#     file=open(filename,"r")
#     if new_name in file:
#         new_name=input("this name already exists, please enter new name!")
#     file.close()
#     return new_name
#
# def printfile (filename):
#     print(filename)
#
# file="c:\lola\ori.txt"
# for i in range (5):
#     details(file)
#
# fruit={"idan","dudu","eli"}
# for i in fruit:
#     print(i)
# test=open("c:\\test\\ori.txt","a")
# test.write("123213123ewqeqw")
# test.close()


# filepath=r"c:\Exercises\IPs.txt"
# file=open(filepath,"w")
# file.write("IPs:\n")
# while 1:
#     ip=input("Please enter IP: ")
#     file.write(ip + "\n")
#     if input("exit?(yes/no)")=="yes":
#         break
# file.close()
#
# iplist=[]
# file=open(filepath,'r')
# for line in file:
#     iplist.append(line)
# file.close()
# print(iplist)
# print(type(iplist))
# new_ip=input("please enter new IP:")
# if new_ip in iplist:
#     print("aaaaaaaaaaaa")
#     iplist.remove(new_ip)
#     file = open(filepath, 'w')
#     for i in range(len(iplist)):
#         file.write(iplist[i])
#     file.close()
# else:
#     print("22222222222")
#     file=open(filepath,'a')
#     file.write(new_ip)
#     file.close()
#
# print(iplist)

#
#
# file=open(filepath,'w')
# for i in range(len(iplist)):
#     file.write(iplist[i])
# file.close()
#
#
#
#
#
# if exists=="1":
#     file=open(filepath,'w')
#     file.close()
#     file=open(filepath,'a')
#     for i in range(len(iplist)):
#         file.write(iplist[i])
#     file.close()
# else:
#     file=open(filepath,'a')
#     file.write(new_ip)
#     file.close()
#
# print (iplist)


# iplist=[]
# file=open(filepath,'r+')
# new_ip=input("please enter new IP: ")
# exists="0"
# for line in file:
#     if new_ip not in line:
#         iplist.append(line)
#     else:
#         exists="1"
# file.close()
#
# if exists=="1":
#     file=open(filepath,'w')
#     file.close()
#     file=open(filepath,'a')
#     for i in range(len(iplist)):
#         file.write(iplist[i])
#     file.close()
# else:
#     file=open(filepath,'a')
#     file.write(new_ip)
#     file.close()
#
# print (iplist)



# new_ip=input("please enter new IP: ")
# exists="0"
# for line in file:
#     print(line)
#     print(type(line))
#     if new_ip in line:
#         line=""
#         exists="1"
# if exists == "0":
#     file.write(new_ip)
# file.close()

myset=set()
for i in range(6):
    myset.add(input("Pleasae enter a name: "))
for i in range (5):
    myset.pop()
os.system("echo /home/ori/Desktop/winnet.txt")






