import turtle

category_totals = {}  # I defined it because I use it in functions.
budgets_of_categories = {}  # I defined it because I use it in functions.
def add_expense():  # A function that allows the user to add expenses and their details
    global category_totals  # If I am going to modify it within the function, I need to activate it
    while True:
        answer = input("How many expenses do you want to enter?: ")
        if answer.isdigit():  # It checks if it consists of numbers
            answer = int(answer)
            break
        else:
            print("Please enter a valid positive integer.")
    for i in range(answer):  # The section where the user enters the details of their expenses
        while True:
            year = input("Please enter the year:")
            if len(year) == 4 and year.isdigit():  # It must be 4 digits
                break
            else:
                print("Please enter the true date!")
        while True:
            month = input("Please enter the month:")
            if month.isdigit() and len(month)==2 and int(month) <= 12 and int(month) >= 1:  # It must consist of numbers and be between 1 and 12
                break
            else:
                print("Please enter the true date!")
        while True:
            day = input("Please enter the day:")
            if day.isdigit() and len(day)==2 and int(day) <= 31 and int(day) >= 1:  # It must consist of numbers and be between 1 and 31
                break
            else:
                print("Please enter the true date!")
        while True:
            amount = input("Please enter the amount:")
            if amount.replace('.', '', 1).isdigit() and amount.count('.') <= 1:  #It checks if the input contains exactly one '.' and, after removing the '.', consists of numbers
                amount=float(amount)
                break
            else:
                print("Please enter a valid positive integer or float.")
        category = input("Please enter the category:").lower()
        description = input("Please enter the description:")
        with open("expenses.txt", "a") as file:  # It saves the user's inputs to a file
            file.write(f" {year}-{ month }-{ day}\t{amount}\t{category}\t{description}\n")
    amount_of_category()  # It calls a function that categorizes the inputs and saves them at the end of the addition
    print("The expense has been added successfully.\n")
    print("Please enter to menu")
    input()




def amount_of_category():  # A function that reads the 'expenses' file and categorizes the entries
    global category_totals  # If I need to modify it within the function, I need to activate it
    category_totals = {}   # I need to define it as empty in order for it to be updated when I run it
    with open("expenses.txt", "r") as file3:  # It reads my file line by line and makes it a list element
        for line in file3:
            lst2 = line.split("\t")  # It splits each element by spaces and lists them again
            if len(lst2) >= 3:  # It checks the number of elements
                category = lst2[2]
                amount = float(lst2[1])
                if category in category_totals:
                    category_totals[category] += amount  # If present, it updates by adding them together
                else:
                    category_totals[category] = amount  # If not present, it adds a new entry

def view_expenses():  # A function that reads the 'expenses' file
    with open("expenses.txt","r") as file1:
        print(file1.read())
    print("Please enter to menu")
    input()

def bar_chart():  # It displays the categories using a graph
    amount_of_category()
    wn = turtle.Screen()
    alex = turtle.Turtle()
    global category_totals  # If I need to modify it within the function, I need to activate it
    xs =list(category_totals.keys())
    maxheight = max(category_totals.values())
    numbars = len(xs)
    border = 10
    wn.setworldcoordinates(0 - border, 0 - border, 40 * int(numbars) + border, maxheight + border)  #Set boundaries to prevent the inputs from going off the screen
    wn.bgcolor("lightgreen")
    alex.color("blue")
    alex.fillcolor("red")
    alex.pensize(3)
    alex.speed(0)
    for i,k in category_totals.items():
        alex.begin_fill()
        alex.left(90)
        alex.forward(int(k))
        alex.write(k)
        alex.right(90)
        alex.forward(40)
        alex.write(i)
        alex.right(90)
        alex.forward(int(k))
        alex.left(90)
        alex.end_fill()
    wn.exitonclick()
def search_filter():  #A function that displays the expression the user wants to search for
    while True:
        search_term = input("Please enter the keyword:")
        matching_expenses = []  # I defined an empty list to display the search results
        with open("expenses.txt", "r") as file:
            for line in file:
                if search_term.lower() in line:  # To avoid issues with uppercase and lowercase letters
                    matching_expenses.append(line)

        if matching_expenses:  # It reads the search results one by one using a for loop
            print("\nSearch Results:")
            for expense in matching_expenses:

                print(expense)
            print("Please enter to menu")
            input()
            break
        else:   # If no search result is found
            print(f"'No results found for '{search_term}'.'")

def update_budgets_of_categories():  # A function that refreshes the old data every time the application is started
    global budgets_of_categories # If I need to modify it within the function, I need to activate it
    with open("budget.txt","r") as file:
        lst = file.readlines()  # It makes each line a list element one by one
        for line in lst:
            lst2 = line.split("\t")  # It splits the line into list elements based on spaces
            if len(lst2) >= 1:
                category = lst2[0] # It finds the category
                total = lst2[1].strip("\n")  # It takes the element without spaces
                budgets_of_categories[category] = total  # It adds the categories with their budgets

def add_budget():  # A function that allows the user to enter their budget
    update_budgets_of_categories()   # I called this function to retain the old information
    global budgets_of_categories # If I need to modify it within the function I need to activate it
    add = input("What is the category you want to choose?:")
    if add in budgets_of_categories.keys():   # If the category exists it updates the budget
        while True:
            a = input("What is your budget of that category?:")
            if a.replace('.', '', 1).isdigit() and a.count('.') <= 1:
                a=float(a)
                break
            else:
                print("Please enter a valid positive integer or float.")
        budgets_of_categories[add] = a
        with open("budget.txt","w") as file: # It adds the data to the budget file at the end.
            for key,value in budgets_of_categories.items():
                file.write(f"{key}\t{value}\n")
    else: # If the category does not exist, it adds a new entry.
        while True:
            b = input("What is your budget of that category?:")
            if b.replace('.', '', 1).isdigit() and b.count('.') <= 1:
                a=float(b)
                break
            else:
                print("Please enter a valid positive integer or float.")
        budgets_of_categories[add] = b
        with open("budget.txt","a") as file: # It adds the data to the budget file at the end.
            file.write(f"{add}\t{b}\n")


def budget_alert():  # The user checks whether they have exceeded the budget in any category.
    amount_of_category()  # I called this function to retain the old information.
    update_budgets_of_categories() # I called this function to retain the old information.
    for key,value in category_totals.items():
        if key not in budgets_of_categories:
            print(f"{key} has not budget.Please add budget of {key}.")
            add_budget()  # I called the function to add it if there is no budget value.
            if float(category_totals[key]) >= float(budgets_of_categories[key]):
                print(f"Warning! {key} exceeds your budget!")  # warning
        else:
            if float(category_totals[key]) >= float(budgets_of_categories[key]):
                print(f"Warning! {key} exceeds your budget!")  # warning
    print("Please enter to menu")
    input()


def view_by_categories():  # A function that allows the user to view their expenses by category.
    with open("expenses.txt", "r") as file:
        lines = file.readlines()  # It listed the data from the expense file.
    categories = {}  # Then, I defined an empty dictionary for later use.
    for line in lines:
        fields = line.strip().split("\t")  # It listed the information from each entry.
        if len(fields) >= 3:
            category = fields[2]  # It found the one with a category.
            if category not in categories:
                categories[category] = []  # If the category doesn't exist, it added it to the dictionary as an empty list.
            categories[category].append(line.strip())  # It added an entry to the list of the value in the dictionary.
    for category, items in categories.items():
        print(f"Kategori: {category}") #It specifies which category it belongs to.
        for item in items:
            print(f"  {item}") # It sorts the data in that category.
        print("-" * 40)  # It sets a boundary between categories.
    print("Please enter to menu")
    input()



def menu(name): # A function that presents the options the user can choose from.
    while True:
        print(f"Welcome {name}")
        print("1. Add Expenses")
        print("2. View  Expenses")
        print("3. Produce Bar Chart of Expenses")
        print("4. Search Filter")
        print("5. Budget Alert")
        print("6. Add Budget")
        print("7. View By Category")
        print("8. Exit")

        choice = input("please choose one number: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice=="3":
            bar_chart()
        elif choice=="4":
            search_filter()
        elif choice =="5":
            budget_alert()
        elif choice== "6":
            add_budget()
        elif choice== "7":
            view_by_categories()
        elif choice == "8":
            print("Have a nice day.Goodbye!")
            break
        else:
            print("Invalid selection! Please try again.")

menu("deniz")