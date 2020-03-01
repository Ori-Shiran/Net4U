
def menu():
    while 1:
        choice=input('''Welcome to Trivago!
        please chose from the menu:
        1. Check available rooms.
        2. Make Reservation.
        3. Cancel Reservation.
        4. Add Nights\Rooms for Reservation. ''')

        if choice=="1":
            var1=["ori",["1","2","3"],["400","450"],["2"]]
            file_path=r"C:\Exercises\Hotels\test.txt"
            file=open(file_path,'a')
            file.write(str(var1))
            file.close()
            print(var1[2])
            file=open(file_path,'r')
            for line in file:
                var2=list(line)
                print(type(var2))
                print(var2)
                print(var2[1])
                print(var2(1)[1])



        # elif choice=="2":
        #
        # elif choice=="3":
        #
        # elif choice=="4":

        else:
            print("Please chose 1-4 from the menu above.")




menu()
