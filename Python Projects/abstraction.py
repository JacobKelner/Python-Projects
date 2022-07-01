

from abc import ABC, abstractmethod
class job(ABC):
    def payStub(self,amount):
        print("Your paycheck amount: ",amount)
    #this function is passing in an argument
    @abstractmethod
    def payment(self,amount):
        pass

class DebitCardPayment(job):
#defining how to implement payment function from parent payStub class
    def payment(self,amount):#this function must have the same name as 'job' class def
        print('Your paycheck amount of {} does not meet the $1250 required for this months rent '.format(amount))
obj = DebitCardPayment()
obj.payStub("$550")
obj.payment("$550")

