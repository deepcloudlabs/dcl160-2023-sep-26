"""
Domain: Core Banking
"""
from enum import Enum
from random import randint


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


class InsufficientBalanceError(Exception):
    def __init__(self, message: str, deficit: float):
        self.message = message
        self.deficit = deficit


class Withdrawble:

    def withdraw(self, amount: float) -> float:
        pass


class Depositable:

    def deposit(self, amount: float) -> float:
        pass


class Account(Withdrawble, Depositable):
    """
    Account is a class -> abstraction
    Members:  i) attributes/state/data -> iban, balance, status, ...
             ii) methods -> dynamic behaviour: withdraw, deposit
                 special methods: constructor (__init__), ...
    """

    def __init__(self, iban: str = "tr1", balance: float = 50, status: AccountStatus = AccountStatus.ACTIVE):
        """
        Constructor
        :param iban: international bank account number
        :param balance: the amount saved in the account
        :param status: the status of the account, e.g. ACTIVE, CLOSED, etc.
        """
        self._iban = iban
        self._balance = balance
        self._status = status

    def __str__(self):
        return f"Account [iban: {self.iban}, balance: {self.balance}, status: {self.status.name}]"

    @property
    def iban(self):
        return self._iban

    @property
    def balance(self):
        return self._balance

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if not self._status == AccountStatus.CLOSED:
            self._status = new_status

    def deposit(self, amount: float) -> float:
        """
        deposit some amount to the balance
        :param amount: amount to deposit. amount should be a positive float. if it is less than or equal
           to zero the method raises ValueError
        :returns the balance after deposit
        """
        # validation rule
        if amount <= 0.0:
            raise ValueError("You must provide a positive amount to deposit")
        # policy
        if not self._status == AccountStatus.ACTIVE:
            raise ValueError(f"Account is not ACTIVE to deposit: {self._status.name}")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        print("Account::withdraw")
        # validation rule
        if amount <= 0.0:
            raise ValueError("You must provide a positive amount to withdraw")
        # policy
        if not self._status == AccountStatus.ACTIVE:
            raise ValueError(f"Account is not ACTIVE to withdraw: {self._status.name}")
        # business rule
        if amount > self._balance:
            deficit = amount - self._balance
            raise InsufficientBalanceError("Your balance does not cover your expenses", deficit)
        self._balance -= amount
        return self._balance


"""
 CheckingAccount: sub-class / derived class
 Account        : super-class / base class
"""


class CheckingAccount(Withdrawble, Depositable):
    def __init__(self, iban: str = "tr1", balance: float = 50, status: AccountStatus = AccountStatus.ACTIVE,
                 overdraft_amount: float = 1_000):
        self._iban = iban
        self._balance = balance
        self._status = status
        self._overdraft_amount = overdraft_amount

    @property
    def overdraft_amount(self):
        return self._overdraft_amount

    def withdraw(self, amount: float) -> float:
        print("CheckingAccount::withdraw")
        # validation rule
        if amount <= 0.0:
            raise ValueError("You must provide a positive amount to withdraw")
        # policy
        if not self._status == AccountStatus.ACTIVE:
            raise ValueError(f"Account is not ACTIVE to withdraw: {self._status.name}")
        # business rule
        if amount > (self._balance + self._overdraft_amount):
            deficit = amount - self._balance - self._overdraft_amount
            raise InsufficientBalanceError("Your balance does not cover your expenses", deficit)
        self._balance -= amount
        return self._balance

    def __str__(self):
        return f"CheckingAccount [iban: {self.iban}, balance: {self.balance}, status: {self.status.name}, overdraft_amount: {self._overdraft_amount}]"


class SavingsAccount(Withdrawble):
    def __init__(self, iban: str, balance: float, status: AccountStatus = AccountStatus.ACTIVE, days: float = 30):
        self._iban = iban
        self._balance = balance
        self._status = status
        self._days = days


try:
    acc: Account = None
    if randint(0, 1):
        acc = CheckingAccount("tr1", 1_000_000, overdraft_amount=250_000)
    else:
        acc = Account("tr2", 2_000_000)
    print(type(acc))
    acc.withdraw(50_000)
except ValueError as ve:
    print(ve)
except InsufficientBalanceError as ibe:
    print(ibe.message, ibe.deficit)
