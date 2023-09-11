def calculate(n1, n2, operation=""):
    operation = str(operation).strip().capitalize()
    if operation == "Add" or operation == "A":
        print(n1 + n2)
    elif operation == "Subtract" or operation == "S":
        print(n1 - n2)
    elif operation == "Multiply" or operation == "M":
        print(n1 * n2)
    else:
        print(n1 + n2)


calculate(10, 20)
calculate(10, 20, "AdD")
calculate(10, 20, "a")
calculate(10, 20, "A")

calculate(10, 20, "S")
calculate(10, 20, "subTRACT")

calculate(10, 20, "Multiply")
calculate(10, 20, "m")
print("#" * 100)


# -------------------------------------------------------------------------------------------------------------
def addition(*numbers):
    result = 0
    for num in numbers:

        if num == 10:
            continue
        elif num == 5:
            result -= 5
        else:

            result += num

    print(result)


addition(10, 20, 30, 10, 15)
addition(10, 20, 30, 10, 15, 5, 100)
print("#" * 100)


# -------------------------------------------------------------------------------------------------------------
def show_skills(name, *skills):
    print(F"Hello {str(name).capitalize()} Your Skills Is" if len(
        skills) > 0 else f"Hello {name} You Have No Skills To Show")
    for skill in skills:
        print(f"- {skill}")


show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

print("#" * 100)


# -------------------------------------------------------------------------------------------------------------
def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    print(f"Hello {name} Your Age Is {age} And You Live In {country}")


say_hello("Osama", 38, "Egypt")
say_hello()
print("#" * 100)
