#Grade system
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def study(self):
        if self.grade == "A":
            print(f"{self.name} is having good grade {self.grade}")
        elif self.grade == "B":
            print(f"{self.name} is having average grade {self.grade}")
        elif self.grade == "F":
            print(f"{self.name} is having low grade {self.grade}")

S1 = Student("siva","A")
S2 = Student("Hari","B")
S3 = Student("Avis","F")
S1.study()
S2.study()
S3.study()

#Bank account

class BankAccount:

    def __init__ (self,balance=200000):
        self.balance = balance
        
        
    def deposit(self,amount=int(input("Enter the amount for deposit:"))):
        self.balance += amount
        print(f"your balance after deposit {self.balance}")
    def withdraw(self,amount=int(input("enter withdrawal anount: "))):
        if self.balance >= amount:
            self.balance -= amount
            print(f"your balance after withdraw {self.balance}")
        else:
            print(f"Insufficient balance, your current balance is{self.balance}")  
    def current_balanace(self):
        print(f"your current balance is{self.balance}")         
        
b = BankAccount()
b.deposit()
b.withdraw()
b.current_balanace()




