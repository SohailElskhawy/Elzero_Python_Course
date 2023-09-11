from functools import reduce

# First Assigment
#-------------------------------------------------------------------------------------------------------------
# def remove_chars(string):
#     return string[1:-1]
friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# cleaned_list = map(remove_chars,friends_map)


# for i in cleaned_list:
#     print(i)

for f in map((lambda name : name[1:-1]),friends_map):
    print(f)
#------------------------------------------------------------------------------------------------------------

print("#" * 70)

# Second Assigment
#-------------------------------------------------------------------------------------------------------------
def get_names(name):
    return name.endswith("m")


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"] 

names = filter(get_names,friends_filter)

for n in names:
    print(n)

# for m in filter((lambda friend : friend.endswith("m")),friends_filter):
#     print(m)    
#-------------------------------------------------------------------------------------------------------------

print("#" * 70)

# Third Assigment 
#-------------------------------------------------------------------------------------------------------------

def multiplyNums(num1,num2):
    return num1 * num2

nums = [2, 4, 6, 2]    
result = reduce(multiplyNums,nums)
print(result)

result2 = reduce(lambda a,b : a*b,nums)
print(result2)
#-------------------------------------------------------------------------------------------------------------

print("#" * 70)

# Forth Assigment
#-------------------------------------------------------------------------------------------------------------
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")


tResult = enumerate(reversed(skills),50)


for c, skill in tResult:
    if isinstance(skill, (int, float)):
        continue
    
    print(f"{c} - {skill}")

#-------------------------------------------------------------------------------------------------------------      


 
