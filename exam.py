import uuid
from datetime import datetime, timezone


class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4(())) #adds a uique identifier
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def update(self, title=None, amount=None):
        self.title = title 
        self.amount = amount 
        self.updated_at = datetime.now(timezone.utc)
        
        print(f"{self.title} has been updated to {self.amount} at {self.updated_at}")
    
    def to_dict(self):
        return {
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S %Z'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S %Z')
        }



class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        """
        This function adds a new expense to our database
        """
        self.expenses.append(expense) #change database to expenses

        print (f"{expense.title} added successfully")
        return expense.id

    def remove_expense(self, expense_id):
        """
        This function removes an expense from our database
        """
        self.expenses = [x for x in self.expenses if x.id != expense_id]
        #self.database.remove(expense_id)
        print (f"Expense with {expense_id} has been removed!")
         

    def get_expense_by_id(self, expense_id):
        """
        This function gets an expense from our database filtering by id
        """
        i_expense = [i for i in self.expenses if i.id == expense_id]
        return i_expense [0] if i_expense else None

    def get_expense_by_title(self, expense_title):
        """
        This function gets an expense from our database filtering by title
        """
        t_expense = [t for t in self.expenses if t.title == expense_title]
        return t_expense [0]


    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]   
    


