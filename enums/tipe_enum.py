from enum import Enum
class TransactionType(str, Enum):
    def __str__(self):
        return str(self.value)
    INCOME = "income"
    EXPENSE = "expense"
    INVEST = "invest"