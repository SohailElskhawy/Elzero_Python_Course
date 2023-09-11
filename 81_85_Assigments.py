# First Assigments
#-------------------------------------------------------------------------------------------------------------

def reverse_string(my_string):
    
    for i in range(len(my_string) - 1 , -1,-1): # len(my_string - 1) = 5 // -1 is the stopping condition for the loop// -1 to step backwards      
        yield my_string[i]

        
# Reverse The String 
for c in reverse_string("Elzero"):
    
    print(c)
#-------------------------------------------------------------------------------------------------------------
    
# Second Assigment
#-------------------------------------------------------------------------------------------------------------
def myDecorator(func):
    
    def wrapper():
        print("Sugar Added From Decorators")
        func()
        print("#" * 20)
    return wrapper    
    





@myDecorator
def make_tea():
  print("Tea Created")

@myDecorator
def make_coffe():
  print("Coffe Created")



make_tea()


make_coffe()