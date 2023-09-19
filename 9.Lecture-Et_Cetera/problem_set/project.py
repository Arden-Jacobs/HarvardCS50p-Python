from datetime import date
import csv


def main():
    write_income_header()
    write_expense_header()
    income_array = get_income()
    expense_array = get_expense()
    income_total = get_total(income_array)
    expense_total = get_total(expense_array)
    print(f"Total Income: {income_total}")
    print(f"Total Expenses: {expense_total}")

    if expense_total and income_total != None:
        net_income = income_total - expense_total
        print(f"Net Income: {net_income}")


def income_journal(**kwargs):
    return(kwargs)


def expenses_journal(**kwargs):
    return(kwargs)


def get_income():
    today_date = date.today()
    income = ["Income Statement"]
    while True:
        try:
            if input("Would you like to create a new Income entery (Y or N): ") == "Y":
                item = input("Enter child name: ")
                source = input("Enter parent name: ")
                amount = int(input("Enter amount: "))
                income.append(income_journal(date=f"{today_date}", item=item, source=source, amount=amount))
                write_income_enteries(today_date, item, source, amount)
            else:
                break
            ...
        except:
            return False
    return income


def get_expense():
    today_date = date.today()
    expense = ["Expense Statement"]
    while True:
        try:
            if input("Would you like to create a new Expense entry (Y or N): ") == "Y":
                item = input("Enter item name: ")
                supplier = input("Enter supplier name: ")
                amount = int(input("Enter amount: "))
                category = input("Enter expense category: ")  # Prompt for category input
                expense.append(expenses_journal(date=today_date, item=item, supplier=supplier, amount=amount, category=category))
                write_expense_enteries(today_date, item, supplier, amount, category)
                expenses_by_category(category,amount)
            else:
                break
            ...
        except:
            return False
    return expense


def get_total(data):
    total = 0
    for i in range(len(data)):
        if i != 0:
            for k,v in data[i].items():
                if k == 'amount':
                    total += v
    return total


def write_income_header():
    with open("Income_Journal.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "item", "source", "amount"])
        writer.writeheader()


def write_expense_header():
    with open("Expense_Journal.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "item", "supplier", "amount", "category"])
        writer.writeheader()


def write_income_enteries(today_date, item, source, amount):
    try:
        with open("Income_Journal.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "item", "source", "amount"])

            writer.writerow({"date": f"{today_date}", "item": item, "source": source, "amount": amount})
    except:
        pass


def write_expense_enteries(today_date, item, supplier, amount, category):
     try:
        with open("Expense_Journal.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "item", "supplier", "amount", "category"])
            writer.writerow({"date": f"{today_date}", "item": item, "supplier": supplier, "amount": amount, "category": category})
     except:
         pass