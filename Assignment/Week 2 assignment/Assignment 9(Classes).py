# Task 1
print("\n ---- Task 1 ----\n")

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name={self.name!r}),(age = {self.age!r})"





s = Student("Ankush", 20)

print("student infomation",s.name,s.age)

print(s)


# Task 2
print("\n ---- Task 2 ----\n")

class Bankaccount:
    def __init__(self,Account_Number,Account_Holder_Name,Balance=0.0):
        self.Account_Number = Account_Number
        self.Account_Holder_Name = Account_Holder_Name
        self.Balance = float(Balance)

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("The Entered Amount is Invalid")
        self.Balance +=amount
        return self.Balance


    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("The Entered Amount is Invalid")
        if amount > self.Balance:
            raise ValueError("Insufficient Balance")
        self.Balance -=amount
        return self.Balance
    def check_Balance(self):
        return self.Balance

    


acct = Bankaccount(1245637373576,"Ankush", 10000.0)
print("Initial Account Balance",acct.check_Balance())
try:
    acct.deposit(5000)
except ValueError as e:
    print("Error: ",e)
acct.withdraw(2000)
print("Current Account Balance",acct.check_Balance())




# Task 3
print("\n ----- Task 3 ----\n")

class Book_Details:
    def __init__(self,Title,Author):
        self.Title = Title
        self.Author = Author

    @classmethod
    def from_string(cls,book_details):
        split_details = [p.strip() for p in book_details.split(" , ",1)]
        if len(split_details) != 2:
            raise ValueError("Invalid book deatils format add both Title and Author")
        return cls(split_details[0] ,split_details[1])

book1 = Book_Details.from_string("The Great Gatsby , F .Scott Fitzgerald")
print("Book Title : ",book1.Title)
print("Book Author : ",book1.Author)