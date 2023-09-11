# First Assigment
#------------------------------------------------------------------------------------------------------------------------------------
# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10"
# "Days From 2021-06-25 To 2021-08-10 Is => 46"


import datetime as dt

theDate = dt.datetime(2021, 6, 25)
todayDate = dt.datetime(2021, 8, 10)

print(f"Days From {theDate} to {todayDate} Is => {(todayDate-theDate).days}")
#-------------------------------------------------------------------------------------------------------------------------------------

print("#" * 70)

# Second Assigment
#-------------------------------------------------------------------------------------------------------------------------------------
# Today Is "2021, 8, 10"

# "2021-08-10" done
# "Aug 10, 2021" done
# "10 - Aug - 2021" done
# "10 / Aug / 21" done
# "10 / August / 2021" done 
# "Tue, 10 August 2021"done

today_Date = dt.datetime(2021, 8, 10)

print(today_Date.strftime("%Y-%m-%d"))
print(today_Date.strftime("%b %d , %Y"))
print(today_Date.strftime("%d - %b - %Y"))
print(today_Date.strftime("%d / %b / %y"))
print(today_Date.strftime("%d / %B / %Y"))
print(today_Date.strftime("%a, %d %B %Y"))
#-------------------------------------------------------------------------------------------------------------------------------------
print("#" * 70)

