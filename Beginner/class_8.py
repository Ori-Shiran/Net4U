from Beginner.myclass import *
Idan=Docs("eyes","haifa","sunday",["2","3","4","5"])
Ahmed=Docs("hands","natanya","monday",["2"])
print("Avilable Doctors:Idan, Ahmed" )

var=input("Enter Doctor name please:")
if var == "Idan":
    Idan.print_details()
    Idan.schedule()
    print(Idan.hours)
elif var =="Ahmed":
    Ahmed.print_details()
    Ahmed.schedule()
    print(Ahmed.hours)
else:
    print("Invalid Doctor name.")
