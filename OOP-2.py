class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance: ", self.balance)
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance: ", self.balance)
    
    def get_balance(self):
        print("Rs.", self.balance)
    
acc1 = Account(1000, 12345)
acc1.debit(700)
acc1.credit(200)
acc1.get_balance()