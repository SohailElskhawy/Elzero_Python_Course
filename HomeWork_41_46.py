# num1 = int(input("Enter Number ").strip())
# num2 = int(input("Enter Number ").strip())

# operation = input("Enter Operation:(+,-,*,/,%)" ).strip()
# print(f"{num1} operation {operation} {num2}")
# if operation == "+":
# print(num1 + num2)
# elif operation == "-":
#   print(num1 - num2)
# elif operation == "*":
#   print(num1 * num2)
# elif operation == "/":
#   print(num1 / num2)
# elif operation == "%":
#   print(num1 % num2)

# age = 15
# print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")

# country = input("Input Your Country ").capitalize().strip()
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# price = 100
# discount = 30

# if country in countries:
#   print(f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}")
# else:
#   print(f"Your Country Not Eligible For Discount And The Price Is ${price}")


admins = ["Sohail", "Malek", "Marwa", "Mohamed", "Ali", "Ahmed", "Sara"]

name = input("Enter Your Name Please ").strip().capitalize()

if name in admins:
    print(f"Welcome Back {name}")
    option = input("Do You Want to Delete or Update name ? ").strip().capitalize()
    if option == "Delete" or option == "D":
        admins.remove(name)
        print("Name Deleted")
        print(admins)
    elif option == "Update" or option == "U":
        TheNewName = input("Enter Your New Name Please ").strip().capitalize()
        admins[admins.index(name)] = TheNewName
        print("Name Updated")
        print(admins)
    else:
        print("Wrong Option")
else:
    status = input("You Are Not An Admin Do You Want to sign up? (Yes or No) ").strip().capitalize()
    if status == "Yes" or status == "Y":
        admins.append(name)
        print("You Have Been Added")
        print(admins)
    elif status == "No" or status == "N":
        print("You are not added")
    else:
        print("Error Try Again")










