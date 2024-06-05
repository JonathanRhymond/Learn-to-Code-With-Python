class Employee():
    def do_work(self):
        print("I'm Working")

class Manager(Employee):
    def waste_time(self):
        print("Wow this youtube video looks fun!")

class Director(Manager):
    def fire_employee(self):
        print("You're fired!")

e = Employee()
m = Manager()
d = Director()

e.do_work()
# e.waste_time()
m.do_work()
m.waste_time()
# m.fire_employee()
d.fire_employee()
