from expense import Expense
from tracker import Tracker
from visualize import plot_pie_chart, plot_bar_chart, plot_line_chart

if __name__ == "__main__":
    """
    expense_obj = Expense(6.52, "abonnement", "2022-03-01", "chatgpt")
    print(expense_obj)
    tracker = Tracker()
    tracker.add_expense(expense_obj)
    
    tracker = Tracker()
    print("-------------------------Expenses----------------------------")
    tracker.load_expenses()
    print("-------------------------Top Expenses----------------------------")
    tracker.get_top_expenses()
    print("-------------------------Total Spending----------------------------")
    tracker.get_total_spending()
    print("-------------------------Spending by Category----------------------------")
    tracker.get_spending_by_category()
    """
    plot_pie_chart()
    plot_bar_chart()
    plot_line_chart()
