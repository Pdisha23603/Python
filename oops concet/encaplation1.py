# 


class Bank:
    def __init__(self, balance):
        self.__balance = balance #private variable
    
    def deposit(self,amount):
        self.__amount += amount 
    def get_balance(self):
        return self.__balance

b1 = Bank(1000)
print(b1.get_balance())