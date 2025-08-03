class checkbalance:
    def __init__(self,name,balance):
        self.name=name
        self.balanace=balance
    def Depositemoney(self,amount):
        self.balanace+=amount
        print("amount deposited:",amount)
    def withdraw(self,amount):
        if amount>self.balanace:
            print("insufficient balance")
        else:
            self.balanace-=amount
            print("amount withdraw is",amount)
    def check_balanace(self):
        print("current balance is:",self.balanace)
bank=checkbalance("deepika",1000)
bank.check_balanace()
bank.Depositemoney(500)
bank.withdraw(300)
bank.check_balanace()
        
        



