
from abc import ABC, abstractmethod

class BaseAccount(ABC):
    def __init__(self, accountNo:str, interest:float):
        self.__AccountNo = accountNo
        self.__Balance = 0
        self.__Interest = interest

    def GetSaldo(self)-> int:
        return self.__Balance

    @abstractmethod
    def Withdraw(self, amount:int)->bool:
        pass

    def GetKontonummer(self)-> int:
        return self.__AccountNo

    def Deposit(self, amount:int):
        amount = amount - 10
        self.__Balance = self.__Balance + amount


class SavingsAccount (BaseAccount): # Sparkonto
    def __init__(self, accountNo:str):
        super().__init__(accountNo, 1.0)

    def Withdraw(self, amount:int) -> bool:
        if amount > 10000:
            return False
        if amount > self.__Balance:
            return False
        self.__Balance = self.__Balance - amount

class SalaryAccount (BaseAccount): # Lönekonto
    def __init__(self, accountNo:str):
        super().__init__(accountNo, 0.1)

    def Withdraw(self, amount:int) -> bool:
        if amount > self.__Balance:
            return False
        self.__Balance = self.__Balance - amount




konto3 = BaseAccount("111123", 4.0)
konto3.Deposit(323)

konto1 = SalaryAccount("121212")
konto1.Deposit(200)

konto2 = SavingsAccount("121213")
konto2.Deposit(100)


print(f"{konto1.GetKontonummer()} : {konto1.GetSaldo()}")

