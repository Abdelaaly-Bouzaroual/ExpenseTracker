import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_pie_chart(filename='expense_obj.csv'):
    df = pd.read_csv(filename)
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')  # Convert to float
    category_spending = df.groupby('category')['amount'].sum()
    plt.figure(figsize=(8, 6))
    plt.pie(category_spending, labels=category_spending.index, autopct='%1.1f%%', startangle=140)
    plt.title("Spending Breakdown by Category")
    plt.show()


def plot_bar_chart(filename='expense_obj.csv'):
    df = pd.read_csv(filename)
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    category_spending = df.groupby('category')['amount'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='category', y='amount', data=category_spending)
    plt.xlabel("Category")
    plt.ylabel("Total Spending")
    plt.title("Total Spending Per Category")
    plt.xticks(rotation=45)
    plt.show()

def plot_line_chart(filename='expense_obj.csv'):
    df = pd.read_csv(filename)
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    daily_spending = df.groupby('date')['amount'].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(daily_spending.index, daily_spending.values, marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel("Total Spending")
    plt.title("Spending Trend Over Time")
    plt.xticks(rotation=45)
    plt.show()
