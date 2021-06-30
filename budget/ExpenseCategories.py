

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

    mysetup = f"from budget.Expense import Expense " \
              f"\nexpenses = Expense.Expenses() " \
              f"\nexpenses.read_expenses('data/spending_data.csv')"

    timetaken_for_loop = timeit.timeit(stmt=expenses.categorize_for_loop, setup=mysetup, number=1000000,globals=globals())

    timetaken_for_set = timeit.timeit(stmt=expenses.categorize_set_comprehension, setup=mysetup, number=1000000, globals=globals())

    if timetaken_for_loop > timetaken_for_set:
        print(f"It is faster in this case with a set, with a set it only took {timetaken_for_set:.1f}s")
    else:
        print(f"Its faster in this case with a loop, with a loop it only took {timetaken_for_loop:.1f}s")


    fig,ax = plt.subplots()
    labels = 'Necessary', 'Food', 'Unnecessary'
    divided_expenses_sum = []

    for category_exps in divided_set_comp:
        divided_expenses_sum.append(sum(x.amount for x in category_exps))

    ax.pie(divided_expenses_sum, labels = labels, autopct = '%1.1f%%')
    plt.show()

if __name__ == "__main__":
    main()