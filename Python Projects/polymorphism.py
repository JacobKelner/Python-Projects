
#Parent class
class User:
    name = "Chandler"
    email = "cbing@gmail.com"
    password = "drowssap"

    def loginInfo(self):
        e_name = input("Enter your name: ")
        e_email = input("Enter your email: ")
        e_password = input("Enter your password: ")
        if (e_email == self.email and entry_password == self.password):#if email and password match, prints next statement
            print("Welcome back, {}!".format(e_name))
        else:
            print("The password or email is incorrect.")#if email or password dont match, prints this statement


#child class employee
class Employee(User):
    pay = 11.00
    department = "Front Desk"
    pin = "1234"

#this is the same method i n the parent class 'User'
#The difference is that, instead of using e_password, its using pin.

    def loginInfo(self):
        e_name = input("Enter your name: ")
        e_email = input("Enter your email: ")
        e_pin = input("Enter your pin: ")
        if (e_email == self.email and e_pin == self.pin):
            print("Welcome back, {}!".format(e_name))
        else:
            print("The pin or email was incorrect")
#this below code invokes the methods inside each class for 'User' and 'Employee'

customer = User()
customer.loginInfo()

manager = Employee()
manager.loginInfo()
