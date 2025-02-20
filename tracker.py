import csv
from linecache import cache

import pandas as pd


class Tracker:
    def __init__(self, filename='expense_obj.csv'):
        self.filename = filename

    def add_expense(self, expense):
        fieldnames = ['amount', 'category', 'date', 'description']

        with open(self.filename, 'a+', newline='') as csvfile:
            csvfile.seek(0)
            file_empty = csvfile.read(1) == ""

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if file_empty:
                writer.writeheader()

            # Convert Expense object to a dictionary and write it
            writer.writerow({
                'amount': expense.amount,
                'category': expense.category,
                'date': expense.date,
                'description': expense.description
            })

    def load_expenses(self):
        try:
            df= pd.read_csv(self.filename)
            print(f'---------------------------------------------------------------------------')
            print(df.head())
            return df
        except FileNotFoundError:
            print(f'File not found {self.filename}')
            return pd.DataFrame(columns=['amount', 'category', 'date', 'description'])

    def get_total_spending(self):
        df = pd.read_csv(self.filename)
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')  # Convert to float
        total_spent = df['amount'].sum()
        print(f"Total Spending: {total_spent}")
        return total_spent

    def get_spending_by_category(self):
        df = pd.read_csv(self.filename)
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')  # Convert to float
        category_spending = df.groupby('category')['amount'].sum()
        print("Spending by Category:\n", category_spending)
        return category_spending

    def get_top_expenses(self):
        df = pd.read_csv(self.filename)
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')  # Convert to float
        top_expenses = df.sort_values(by='amount', ascending=False).head(10)  # Sort full DataFrame
        print("Top 10 Expenses:\n", top_expenses)
        return top_expenses





