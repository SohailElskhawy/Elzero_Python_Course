# First Assigment
# -----------------------------------------------------------------------------------------------
my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
  my_data.append("".join(map(str,data)))                #my_data = [(E,L),(Z,E),(R,O)]

final_string = "".join(my_data)
final_string = final_string.title()
print(final_string) # Elzero
# -----------------------------------------------------------------------------------------------

print("#" * 70)
# Second Assigment
# -----------------------------------------------------------------------------------------------
my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    my_data.append(item1)

final_string = "".join(str(item) for item in my_data[:6])
print(final_string.title())
# -----------------------------------------------------------------------------------------------
print("#" * 70)

# Forth Assigments
# -----------------------------------------------------------------------------------------------

# Write Function With Help To Get The Output
def say_hello_to(name):
  
  """ 
  parameter(someone) => Person Name
  Function To Say Hello To Anyone
  """
  return f"Hello {name}"

print(say_hello_to("Osama")) # "Hello Osama"
# Write Doc String Line For The Function Here

# Function Doc String Output
"parameter(someone) => Person Name"
"Function To Say Hello To Anyone"
print(say_hello_to.__doc__)
# ----------------------------------------------------------------------------------------------
print("#" * 70)
# Fifth Assigment
# ----------------------------------------------------------------------------------------------


myFriends = ["Ahmed", "Osama", "Sayed"]

def sayHello(SomePeoples) -> list:
  for Someone in SomePeoples:
    print(f"Hello {Someone}")

sayHello(myFriends)