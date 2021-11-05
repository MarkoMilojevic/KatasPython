from __future__ import annotations
from datetime import datetime


class Account:
    def __init__(self: Account) -> None:
        # List of tuples (timestamp, amount, balance)
        self._transactions: tuple[datetime, int, int] = []

    def deposit(self: Account, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Deposited amount must be a positive value.")

        balance: int = self._balance()
        self._transactions.append((datetime.now(), amount, balance + amount))

    def withdraw(self: Account, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Withdrawn amount must be a positive value.")

        balance: int = self._balance()

        if amount > balance:
            raise ValueError("Not enough funds on your account.")

        self._transactions.append((datetime.now(), -amount, balance - amount))

    def _balance(self: Account) -> int:
        return sum([amount for _, amount, _ in self._transactions])

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
