# https://leetcode.com/problems/simple-bank-system/

class Bank:

    def __init__(self, balance: List[int]):
        self.balance = [None]
        for money in balance:
            self.balance.append(money)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid_id(account1) or not self.is_valid_id(account2):
            return False

        if not self.has_enough_money(account1, money):
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid_id(account):
            return False

        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid_id(account):
            return False

        if not self.has_enough_money(account, money):
            return False
        self.balance[account] -= money
        return True

    def is_valid_id(self, id):
        return id >= 1 and id < len(self.balance)

    def has_enough_money(self, id, money):
        return self.balance[id] >= money

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
