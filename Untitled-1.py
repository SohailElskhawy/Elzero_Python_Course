def myMax(*args):
    
    a = list(*args)
    a.sort(reverse=True)
    
    
    return  a[0]


print(myMax([1,-8,10,74,100,25,19,-70]))
print("#" * 60)


def myMin(*nums):
    
    b = list(*nums)
    b.sort()
    
    
    return  b[0]


print(myMin((1,-8,10,74,100,25,19,-70)))