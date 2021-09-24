class Atm():
    def __init__(self,cardNumber,pin):
        
        
        self.cardNumber=cardNumber
        self.pin=pin


    def BalanceEnquiry():
        balance=1000
        print("you have "+balance+"in your account")
    
    def CashWithDraw():
        print("you have withdrawed your money")
        

card=Atm("168493","1234")