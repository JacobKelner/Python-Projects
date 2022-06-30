#creating a base class
class Base:
    def __init__(self):
        self._var = 23 #protected variable

obj1 = Base()#assigns class to variable (obj1)

print(obj1._var)#calling protected variable



class baseAgain:
    def __init__(self):#function
        self.__c = "Learning to code is a fun challenge!"#self is used to acess variables within this class

    def getPrivate(self):#another function 
        print(self.__c)#self.__c is called from the above function 

    def setPrivate(self, private):#private is a new variable that we list inside the parameter
        self.__c = private#private is given its value from self.__c


obj = baseAgain()#calls class to obj
obj.getPrivate()#calls and prints function
obj.setPrivate("The above statement is agreeable")
obj.getPrivate()



        
        
