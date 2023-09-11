# First Assigment
#---------------------------------------------------------------------------------------------------------------------
# values = (0, 1, 2) #false, true , true

# if any(values): #If there is a least a true value

#   my_var = 0

# my_list = [True, 1,  1, ["A", "B"], 10.5, my_var] # my_var = 0

# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]): # if all value in this lists are true  so we print good

#   print("Good")

# else:

#   print("Bad")
  
#  Good  

#---------------------------------------------------------------------------------------------------------------------

# Second Assigment
#---------------------------------------------------------------------------------------------------------------------
# v = 40

# my_range = list(range(v))


# print(sum(my_range, v) + pow(v, v, v)) # sum of the list + 0  The Answer is 820 so the v is 40
#---------------------------------------------------------------------------------------------------------------------

# Third Assigment
#---------------------------------------------------------------------------------------------------------------------
# n = 21

# l = list(range(n)) 

# if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

#   print("Good") 
  
# Output is Answer is Good So The n is 21   
#---------------------------------------------------------------------------------------------------------------------


# Forth Assigment
#---------------------------------------------------------------------------------------------------------------------
# def my_all(lists):
#     return all(lists)   
    
# print(my_all([1, 2, 3]))
# print(my_all([1, 2, 3, []]))

# print("#" * 70)

# def my_any(lists):
#     return any(lists)   
    
# print(my_any([0, 1, [], False])) 
# print(my_any([(), 0, False]))

# print("#" * 70)

# def my_min(lists):
#     return min(*lists)
# print(my_min([10, 100, -20, -100, 50]))
# print(my_min((10, 100, -20, -100, 50)))

# print("#" * 70)

# def my_max(lists):
#     return max(*lists)

# print(my_max([10, 100, -20, -100, 50, 700])) 
# print(my_max((10, 100, -20, -100, 50, 700)))    
#---------------------------------------------------------------------------------------------------------------------
# Fifth Assigment
#---------------------------------------------------------------------------------------------------------------------
# def myall(iterable):
#     for element in iterable:
#         if not element:
#          return False
#     return True
# print(myall([1, 2, 3]))
# print(myall([1, 2, 3, []]))

# print("#" * 70)

# def my_any(iterable1):
#     for i in iterable1:
#         if i :
#             return True
#     return False    
# print(my_any([0, 1, [], False])) 
# print(my_any([(), 0, False]))

# print("#" * 70)

# list1 = [10,40,35,60,80]

# list1.sort(reverse=True)


# print(list1[0])

# my_tuple = (10,40,35,60,80)

# smy=sorted(my_tuple,reverse=True)
# print(smy[0])

# def my_min(*args):
#     # Convert args to a single iterable
#     iterable = args[0] if len(args) == 1 else args

#     # Initialize the minimum value with the first element
#     minimum = iterable[0]

#     # Iterate over the iterable to find the minimum value
#     for element in iterable:
#         if element < minimum:
#             minimum = element

#     return minimum
# print(my_min([10, 100, -20, -100, 50])) 
# print(my_min((10, 100, -20, -100, 50))) 
#---------------------------------------------------------------------------------------------------------------------    
    


    
