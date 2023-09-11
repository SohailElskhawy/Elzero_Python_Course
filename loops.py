# name = "Sohail"

# for letter in name:
#   print(f"[{letter}]")


# names = ["Sohail", "Malek", "Ali"]
# fatherName = ["Mohamed"]

# for name in names:
#   for father in fatherName:
#      print(name, father)

names = {
    "Sohail": {
        "English": "80%",
        "Arabic": "90%",
        "Turkish": "60%",
        "Japanese": "40%"

    },
    "Malek": {
        "English": "90%",
        "Arabic": "70%",
        "Turkish": "50%",
        "German": "20%",
        "Japanese": "30%"
    },
    "Marwa": {
        "English": "70%",
        "Arabic": "90%",
        "Turkish": "60%"

    },
    "Mohamed": {
        "English": "80%",
        "Arabic": "90%",
        "Turkish": "70%"
    }

}

for name in names:
    print(f"This is {name} And He Speaks {len(names[name])} Languages")
    for lang in names[name]:
        print(f"{lang} => {names[name][lang]}")

print("#" * 90)
for x in range(1, 11):
    if x % 2 == 0:
        print(f"{x} is an Even Number")
    else:
        print(f"{x} is an Odd Number")
print("#" * 90)
a = int(input("Enter A Number: "))
count = 0
while a > 1:
    a -= 1
    if a == 6:
        continue
    print(a)
    count += 1

else:
    print(f"Loop is done, {count} numbers are printed")
