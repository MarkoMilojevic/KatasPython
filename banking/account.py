from datetime import datetime


class Account:
    def __init__(self) -> None:
        # List of tuples (timestamp: datetime, amount: int, balance: int)
        self._transactions = []

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Deposited amount must be a positive value.")

        balance = self._balance()
        self._transactions.append((datetime.now(), amount, balance + amount))

    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Withdrawn amount must be a positive value.")

        balance = self._balance()

        if amount > balance:
            raise ValueError("Not enough funds on your account.")

        self._transactions.append((datetime.now(), -amount, balance - amount))

    def _balance(self):
        return sum([amount for _, amount, _ in self._transactions])

    def print_statement(self):
        print(f"{'Date':<13}{'Amount':<9}{'Balance':<9}")

        for date, amount, balance in self._transactions:
            print(f"{date.strftime('%d.%m.%Y'):<13}{amount:<+9}{balance:<9}")


def main():
    acc = Account()
    acc.deposit(500)
    acc.withdraw(100)
    acc.print_statement()


if __name__ == "__main__":
    main()
