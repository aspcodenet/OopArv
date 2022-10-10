class BaseAccount:
    def __init__(self, accountNo:str, interest:float):
        self.__AccountNo = accountNo
        self.__Saldo = 0
        self.__Interest = interest

class SavingsAccount (BaseAccount): # Sparkonto
    def __init__(self, accountNo:str):
        super().__init__(accountNo, 1.0)

    def GetSaldo(self)-> int:
        return self.__Saldo

    def GetKontonummer(self)-> int:
        return self.__AccountNo

    def Deposit(self, amount:int):
        amount = amount - 10
        self.__Saldo = self.__Saldo + amount

    def Withdraw(self, amount:int) -> bool:
        if amount > 10000:
            return False
        if amount > self.__Saldo:
            return False
        self.__Saldo = self.__Saldo - amount



class SalaryAccount: # Lönekonto
    def __init__(self, accountNo:str):
        self.__AccountNo = accountNo
        self.__Saldo = 0
        self.__Interest = 0.01

    def GetSaldo(self)-> int:
        return self.__Saldo

    def GetKontonummer(self)-> int:
        return self.__AccountNo

    def Deposit(self, amount:int):
        amount = amount - 10
        self.__Saldo = self.__Saldo + amount

    def Withdraw(self, amount:int) -> bool:
        if amount > self.__Saldo:
            return False
        self.__Saldo = self.__Saldo - amount






konto1 = SavingsAccount("121212")
konto1.Deposit(200)
konto2 = SavingsAccount("121213")
konto2.Deposit(100)
print(f"{konto1.GetKontonummer()} : {konto1.GetSaldo()}")

