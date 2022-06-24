
#Parent class
class User:
    name = "Chandler"
    email = "cbing@gmail.com"
    password = "drowssap"

    def loginInfo(self):
        e_name = input("Enter your name: ")
        e_email = input("Enter your email: ")
        e_password = input("Enter your password: ")
        if (e_email == self.email and e_password == self.password):#if email and password match, prints next statement
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


#child class Social
class Social(User):
    account = "Chandler_Bing"
    followers = "5"
    passcode = "232435127"
#Same method in the parent class 'User'
#the difference is that instead of using e_password, its using passcode and

    def loginInfo(self):
        e_account = input("Enter your account name: ")
        e_email = input("Enter your email: ")
        e_passcode = input("Enter your passcode: ")
        if (e_account == self.account and e_passcode == self.passcode):
            print("Thanks for logging in, {}!".format(e_account))
        else:
            print("Your login information was incorrect, please try again!")


#this below code invokes the methods inside each class for 'User' and 'Employee'

customer = User()
customer.loginInfo()

manager = Employee()
manager.loginInfo()

login = Social()
login.loginInfo()
