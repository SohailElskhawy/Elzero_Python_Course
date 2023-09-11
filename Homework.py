name = 'Elzero'

print("Second Letter", name[1])
print("Third Letter", name[2])
print("Last Letter", name[-1])

print(name[1:4])
print(name[::2])
print(name[4::-2])

name1 = "#@#@Elzero#@#@"
print(name1.strip("#@"))

num = "9"
num1 = "15"
num2 = "130"
num3 = "950"
num4 = "1500"

print(num1.zfill(4))

name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "#"))
print(name_two.rjust(20, "#"))

name_three = "OSamA"
name_four = "osaMA"

print(name_three.swapcase())
print(name_four.swapcase())

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

name2 = "Elzero"
print(name2.find("z"))

msg2 = "I <3 Python And Although <3 Elzero Web School"
print(msg2.replace("<3", "Love", 1))

print((1 + 2j).imag)
print((1 + 2j).real)
print(float(10))
print(int(159.650))
print(type(int(159.650)))

print("=" * 60)

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])
print(len(friends))
print(friends[0::2])
print(friends[1::2])
print(friends[1:4])
print(friends[3:5])
friends[3] = "Elzero"
friends[4] = "Elzero"
print(friends)

friends1 = ["Osama", "Ahmed", "Sayed"]

friends1.insert(0, "Nasser")
print(friends1)
print("=" * 60)
friends1.insert(4, "Nasser")
print(friends1)

print("=" * 60)

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[4][0])
print(technologies[4][2])

friends5 = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends5.sort()
print(friends5)
print("=" * 60)
friends5.sort(reverse=True)
print(friends5)
print("=" * 60)
friends6 = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends6.extend(employees)
friends6.extend(school)
print(friends6)
print("=" * 60)
print("=" * 60)
print("=" * 60)

myTup = ("Sohail", "Malek", "Mohamed", "Marwa")
print(myTup[2])
print("=" * 60)
mylist = list(myTup)
mylist.append("Sayed")
myTup = tuple(mylist)
print(myTup)

a = (1, 2, 3, 4)
for x in a:
    print(x)

print("=" * 60)

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(str(unique_list))
print(type(unique_list))
unique_list.remove(5)
print(str(unique_list))
print("=" * 60)

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters))
print("=" * 60)

my_set = {1, 2, 3}
letters1 = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set = letters1
my_set.remove("C")
print(my_set)

print("=" * 60)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print("=" * 60)

mydict = {"HTML": "90%",
          "CSS": "80%",
          "Python": "30%",
          "AI": "20%"}
print(mydict)

print(mydict.get("HTML"))
print(f"HTML progress is {mydict.get('HTML')}")
print(f"CSS progress is {mydict.get('CSS')}")
print(f"Python progress is {mydict.get('Python')}")
print(f"AI progress is {mydict.get('AI')}")
print("$" * 100)
print("$" * 100 )
for key, value in mydict.items():
    print(f"{key} Progress is {value}")
