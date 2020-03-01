class Docs:
    def __init__(self,prof,city,days,hours):
        self.prof=prof
        self.days=days
        self.city=city
        self.hours=hours

    def print_details(self):
        print("Profasion: " + self.prof + "\nCity: " + self.city + "\nAvilability: Days: " + self.days +". Hours: "+str(self.hours))

    def schedule (self):
        var2=input("Please enter when do you want to schedule from: " +str(self.hours))
        while var2 not in self.hours:
            var2=input("please chose from avilavle hours only! ")
        self.hours.remove(var2)
        print("Your appointment set to: " + var2 +" O'clock, pelase dont be late.")

