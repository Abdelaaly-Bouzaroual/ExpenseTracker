class Expense:
   def __init__(self, amount , category , date , description ):
       self.amount = amount
       self.category = category
       self.date  = date
       self.description  = description

   def __str__(self):
        return (f'The amount is {self.amount} '
                f'\nand the category is {self.category} '
                f'\nand the date is {self.date} '
                f'\nand the description is {self.description}')

   def __repr__(self):
       return self.__str__()