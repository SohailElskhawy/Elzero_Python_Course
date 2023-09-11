# First Assigments 
# --------------------------------------------------------------------------------------------------------
class Game:
# Write Class Content
    def __init__(self,name,developer,year,price) :

        self.name = name
        self.developer = developer
        self.year = year
        self.price = price
    def price_in_pounds(self):
        return f"{self.price * 15.6} Egyptian Pounds"

game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")
# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"
# --------------------------------------------------------------------------------------------------------
print("#" * 70)
# Second Assigment
# ------------------------------------------------------------------------------------------------------------
class User:
# Write Class Content
    def __init__(self,first_name,last_name,age,gender) :
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.gen = gender
    def full_details(self):
        if self.gen == "Male":
            return f"Hello Mr {self.fname} {self.lname[:1]}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"
        elif self.gen == "Female":
            return f"Hello Mrs {self.fname} {self.lname[:1]}. [{str(40 - self.age).zfill(2)}] Years To Reach 40"

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40
# -------------------------------------------------------------------------------------------------------------
print("#" * 70)
# Third Assigment
# ------------------------------------------------------------------------------------------------------------
class Message:
    # Write Class Content
    
    @staticmethod
    def print_message():
        return "Hello From Class Message"


print(Message.print_message())
# Output
# Hello From Class Message
# ------------------------------------------------------------------------------------------------------------
print("#" * 70) 
# Forth Assgiment
# ------------------------------------------------------------------------------------------------------------
class Games:
    def __init__(self,game):
        self.game = game
    def show_games(self):
            if type(self.game) == list:
                print("I Have Many Games:")
                for g in self.game:
                    print(f"-- {g}")
            elif type(self.game) == int:
                print(f"I Have {self.game} Game")
            elif type(self.game) == str:
                print(f"I Have One Game Called \"{self.game}\"")       

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"
print("-" * 20) 
my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin
print("-" * 20) 
my_games_count.show_games()
# Output
# I Have 80 Game.
# ------------------------------------------------------------------------------------------------------------
print("#" * 70) 
# Fifth Assgiment
# ------------------------------------------------------------------------------------------------------------
# Main Class
class Members:

    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members):
    def __init__(self, n, p):
        super().__init__(n, p)
        
# Create Moderators Class Here
class Moderators(Members):
    def __init__(self, n, p):
        Members.__init__(self, n, p)
        



member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator
# ------------------------------------------------------------------------------------------------------------
print("#" * 70) 
# Sixth Assgiment
# ------------------------------------------------------------------------------------------------------------
class A:

    def __init__(self, one):

        self.one = one

class B:

    def __init__(self, two):

        self.two = two

class C:

    def __init__(self, three):

        self.three = three

# Write The Class Called "Text" Here
class Text(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self,one)
        B.__init__(self,two)
        C.__init__(self,three)
        
    def show_name(self):
        return f"The Name Is {self.one}{self.two}{self.three}"

the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero
# ------------------------------------------------------------------------------------------------------------
