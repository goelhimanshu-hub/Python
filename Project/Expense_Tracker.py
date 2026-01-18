print("Welcome to Expense Tracker 💸")
Sum=0
expenses=[]
while True:
    print("======= MENU =======")
    print("1️⃣   Add Expense")
    print("2️⃣   View All Expenses")
    print("3️⃣   View Total Spending")
    print("4️⃣   Exit")
    print("=====================")
    choice=int(input("Enter your choice (1-4): "))

    if choice==1:
        print("Enter date (DD-MM-YY): ",end="")
        date=input()
        print()
        print("Enter category (Food, Travel, Shopping, etc): ",end="")
        category=input()
        print()
        print("Enter short description: ",end="")
        description=input()
        print()
        print("Enter amount (₹): ",end="")
        amount=int(input())
        print()
        expense={   'date':date,
            'category': category,
            'description':description,
            'amount':amount
                    }
        expenses.append(expense)
        Sum=Sum+expense['amount']
        print("✅ Expense added successfully!")
    elif choice==2:
        e=1
        print("🫰View all expenses 🫰")
        for i in expenses:
            print(f"------{e} expenses ----")
            print("-----Date : ",i['date'])
            print("-----Category: ",i['category'])
            print("-----Description: ",i['description'])
            print("-----Amount : ",i['amount'])
            e+=1
            print()
    elif choice==3:
        print(f"Total Spending is :💰 {Sum}")
    elif choice==4:
        print("-------Thank You------")
        break
    