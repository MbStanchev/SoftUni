class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.balance < 0:
            raise ValueError("sorry cannot go in debt!")
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    # def add_transaction(self, amount):
    #     if not amount isinstance(amount, integer):
    #
    #         raise ValueError("please use int for amount")
    #     if self.balance < 0:
    #         raise ValueError("sorry cannot go in debt!")
    #     self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"
