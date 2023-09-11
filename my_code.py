'''
        say hello my friends
'''
my_friends = ["Ahmed", "Osama", "Sayed"]
def say_hello(somepeoples) -> list:
    '''Function Say Hello To Friends in List'''
    for someone in somepeoples:
        print(f"Hello {someone}")
say_hello(my_friends)
