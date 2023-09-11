# First Assigment
#----------------------------------------------------------------------------------------------------
# def get_score(**subjects):
#     for key,value in subjects.items():
#         print(f"{key} => {value}")
# get_score(Math=90, Science=80, Language=70)
# get_score(Logic=70, Problems=60)
#----------------------------------------------------------------------------------------------------        

# Second Assigment
#----------------------------------------------------------------------------------------------------
# def get_people_scores(name="" ,**subjects):
    
#    if len(subjects) == 0:
#        print(f"Hello {name} You Have No Scores To Show")
#    elif len(name) != 0:
#        print(f"Hello {name} This Is Your Score Table:")
#        for key,value in subjects.items():
#            print(f"{key} => {value}")
#    else:
#        for key,value in subjects.items():
#            print(f"{key} => {value}")
        
# get_people_scores("Ahmed")  
# print("#"*10)  
# get_people_scores("Osama", Math=90, Science=80, Language=70)
# print("#"*10)
# get_people_scores("Mahmoud", Logic=70, Problems=60)
# print("#"*10)
# get_people_scores(Logic=70, Problems=60)
#----------------------------------------------------------------------------------------------------


# Third Assigment
#----------------------------------------------------------------------------------------------------
# scores_list = {
#     "Math" : 90,
#     "Science" : 80,
#     "Language" : 70
# }

# def get_the_scores(name="" ,**subjects):
    
#    if len(subjects) == 0:
#        print(f"Hello {name} You Have No Scores To Show")
#    elif len(name) != 0:
#        print(f"Hello {name} This Is Your Score Table:")
#        for key,value in subjects.items():
#            print(f"{key} => {value}")
#    else:
#        for key,value in subjects.items():
#            print(f"{key} => {value}")        
        
# get_the_scores("Osama", **scores_list)
# print("#"*10)
# get_the_scores("Osama")
# print("#"*10)
# get_the_scores(**scores_list)
#----------------------------------------------------------------------------------------------------