import datetime
print("Welcome.")
name=input("What is your name?")
age=int(input('What is your age?'))
print("you where born at:" )
now=datetime.datetime.now()
print("Hi " + name + " you where born at: " + str(now.year-age))
