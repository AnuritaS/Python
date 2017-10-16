'''
Write a parent class “Bank_Acount”. This class has below attributes
Account ID ,AccountHolderName, Balance

The class has three methods
input_values() – Gets the values of attributes from the user.
print_details() – Prints the values of the attributes
computeDraftLimit() – Computes and prints draft limit value , which is 90% of balance amount.

Create a child class called “Current_Account”. Apart from the attributes from the parent class, this child class has two additional attributes – OverDraftLimit, WaiverBalance.

The child class overrides the computeDraftLimit() method to compute and prints draft limit value , which is 120% of balance amount.

Create 2 instances – one of parent and one of child class and demonstrate the functionalities.
'''
class Bank_Account:
    acc_id=0
    name=""
    bal=0
    def __init__(self):
        pass
    def input_values(self):
        self.acc_id=int(input("Enter Account ID? "))
        self.name=input("Enter Account Holder's Name? ")
        self.bal=float(input("Enter balance in the Account? "))
    def print_values(self):
        print("Account ID: ", self.acc_id)
        print("Account Holder's Name: ", self.name)
        print("Balance in the Account: ", self.bal)
    def computeDraftLimit(self):
        return self.bal*0.9
class Current_Account(Bank_Account):
    def __init__(self):
        Bank_Account.__init__(self)
    def computeDraftLimit(self):
        return self.bal*1.2
c= Current_Account()
c.input_values()
print("Details in current account are :")
c.print_values()
print("The Draft Limit is: ", c.computeDraftLimit())
b= Bank_Account()
b.input_values()
print("Details in normal account are :")
b.print_values()
print("The Draft Limit is: ", b.computeDraftLimit())