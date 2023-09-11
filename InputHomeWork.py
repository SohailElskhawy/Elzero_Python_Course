# name = input("What\'s Your Name ")
# name = name.strip().capitalize()
# print(f"Hello {name}, Happy To See You Here. ")
print("#" * 70)

# age = int(input("Enter Your Age: "))

# if age <= 16:

#  print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# elif age > 16:
#  print(f"Hello Your Age Is {age}, All Articles  Suitable For You")

# FirstName = input("Enter Your First Name : ")
# SecondName = input("Enter Your Second Name : ")
# FirstName = FirstName.strip().capitalize()
# SecondName = SecondName.strip().capitalize()

# print(f"Hello {FirstName} {SecondName:.1s}.")


# email = input("Enter Your Email : ")

# email = email.lower().strip()
# nameInEmail = email[:email.index('@')]
# nameInEmail = nameInEmail.capitalize()

# print(f"Your Name Is {nameInEmail}")
# print(f"Email Service Provider Is {email[email.index('@') + 1:email.index('.')]}")
# print(f"Top Level Domain Is {email[email.index('.') + 1:]}")

age = int(input("What\'s Your Age ? ").strip())

if 10 < age < 100:
    months = age * 12
    weeks = months * 4
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print(f'Your Age is {age}')
    print("You Lived For:")
    print(f"{months} Months.")
    print(f"{weeks:,} Weeks.")
    print(f"{days:,} Days.")
    print(f"{hours:,} Hours.")
    print(f"{minutes:,} Minutes.")
    print(f"{seconds:,} Seconds.")
else:
    print("Age is out of bound")




