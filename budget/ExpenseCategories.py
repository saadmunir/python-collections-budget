
from budget.Expense import *
import matplotlib.pyplot as plt

import timeit

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()

    if divided_set_comp != divided_for_loop:
        print("Sets are NOT equal by == test")

    for a,b in zip(divided_for_loop, divided_set_comp):
        if (not a.issubset(b) and b.issubset(a)):
            print("Sets are NOT equal by subset test")

    mysetup = f"import os" \
              f"\ncwd = os.getcwd()" \
              f"\nos.chdir('C:/Users/Agne/Desktop/python-collections-budget')" \
              f"\nfrom budget.Expense import Expense " \
              f"\nexpenses = Expense.Expenses() " \
              f"\nexpenses.read_expenses('data/spending_data.csv')"

    timetaken_for_loop = timeit.timeit(stmt=expenses.categorize_for_loop, setup=mysetup, number=1000000,globals=globals())

    print(f" Timetaken for loop: {timetaken_for_loop}s")

    mysetup2 = f"import os" \
              f"\ncwd = os.getcwd()" \
              f"\nos.chdir('C:/Users/Agne/Desktop/python-collections-budget')" \
              f"\nfrom budget.Expense import Expense " \
              f"\nexpenses = Expense.Expenses() " \
              f"\nexpenses.read_expenses('data/spending_data.csv')"

    timetaken_set_comprehension = timeit.timeit(stmt=expenses.categorize_set_comprehension, setup=mysetup2, number=1000000, globals=globals())

    print(f" Timetaken for comprehension: {timetaken_set_comprehension}s")

    fig,ax = plt.subplots()
    labels = 'Necessary', 'Food', 'Unecessary'
    divided_expenses_sum = []

    for category_exps in divided_set_comp:
        divided_expenses_sum.append(sum(x.amount for x in category_exps))

    ax.pie(divided_expenses_sum, labels = labels, autopct = '%1.1f%%')
    plt.show()

if __name__ == "__main__":
    main()