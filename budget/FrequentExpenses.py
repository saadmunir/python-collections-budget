import os

cwd = os.getcwd()
os.chdir('C:/Users/Agne/Desktop/python-collections-budget')

from budget.Expense import *
import collections
import matplotlib.pyplot as plt

expenses = Expenses()
expenses.read_expenses(filename="data/spending_data.csv")

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)

top5 = spending_counter.most_common(5)

categories, count = zip(*top5)

fig, ax = plt.subplots()

ax.bar(categories, count)

ax.set_title(r"# of Purchases by Category")

plt.show()