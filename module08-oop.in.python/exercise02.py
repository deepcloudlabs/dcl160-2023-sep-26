"""
Domain: Core Banking
"""
from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


class InsufficientBalanceError(Exception):
    def __init__(self, message: str, deficit: float):
        self.message = message
        self.deficit = deficit


class Account:
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


class CheckingAccount(Account):
    def __init__(self, iban: str = "tr1", balance: float = 50, status: AccountStatus = AccountStatus.ACTIVE,
                 overdraft_amount: float = 1_000):
        super().__init__(iban, balance, status)
        self._overdraft_amount = overdraft_amount

    @property
    def overdraft_amount(self):
        return self._overdraft_amount

    def withdraw(self, amount: float) -> float:
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


try:
    acc1 = CheckingAccount("tr1", 1_000_000, overdraft_amount=250_000)  # object
    acc2 = Account("tr2", 2_000_000)  # object
    print(f"balance in acc1 is {acc1.balance}")
    acc1.withdraw(1_250_000)  # withdraw(acc1, 250_000)
    acc2.withdraw(250_000)  # withdraw(acc2, 250_000)
    acc2.deposit(375_000)  # deposit(acc2, 250_000)
    print(acc1)
    print(acc2)
    acc2.status = AccountStatus.BLOCKED
    print(f"status of acc2 is {acc2.status.name}")
    acc2.status = AccountStatus.CLOSED
    print(f"status of acc2 is {acc2.status.name}")
    acc2.status = AccountStatus.ACTIVE
    print(f"status of acc2 is {acc2.status.name}")
except ValueError as ve:
    print(ve)
except InsufficientBalanceError as ibe:
    print(ibe.message, ibe.deficit)
