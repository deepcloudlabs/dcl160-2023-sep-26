"""
Domain: Core Banking
"""
from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300


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
        self.iban = iban
        self.balance = balance
        self.status = status


acc1 = Account("tr1", 1_000_000)  # object
print(f"balance in acc1 is {acc1.balance}")
