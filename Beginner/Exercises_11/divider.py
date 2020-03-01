num=int(input("Please enter a number: "))
counter=1
deviders=[]
while counter < num:
    if num % counter == 0:
        deviders.append(counter)
    counter=counter+1
print("List of divders to your number: " + str(deviders))

# num=int(input("Please enter a number: "))
# for i in range (num, num+1):
#     if num%i==0:
#         print("It Divided by: "+ str(i))