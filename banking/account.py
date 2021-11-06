from __future__ import annotations
from datetime import datetime
from collections import namedtuple

Transaction = namedtuple("Transaction", "timestamp, amount, balance")


class Account:
    def __init__(self: Account) -> None:
        self._transactions: list[Transaction] = []

    def deposit(self: Account, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Deposited amount must be a positive value.")

        balance: int = self._balance()
        self._transactions.append(Transaction(datetime.now(), amount, balance + amount))

    def withdraw(self: Account, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Withdrawn amount must be a positive value.")

        balance: int = self._balance()

        if amount > balance:
            raise ValueError("Not enough funds on your account.")

        self._transactions.append(
            Transaction(datetime.now(), -amount, balance - amount)
        )

    def _balance(self: Account) -> int:
        return sum(map(lambda transaction: transaction.amount, self._transactions))

    def print_statement(self: Account) -> None:
        print(f"{'Date':<13}{'Amount':<9}{'Balance':<9}")

        for date, amount, balance in self._transactions:
            print(f"{date.strftime('%d.%m.%Y'):<13}{amount:<+9}{balance:<9}")


def main() -> None:
    acc = Account()
    acc.deposit(500)
    acc.withdraw(100)
    acc.print_statement()


if __name__ == "__main__":
    main()
