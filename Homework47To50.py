num = int(input("Enter Number That Larger Than 0 "))
count = 0
if num <= 0:
    print(f"Number {num} Is Not Larger Than 0")
else:

    while num > 1:
        num -= 1
        if num == 6:
            continue
        print(num)
        count += 1
print(f"{count} Numbers Printed Successfully.")
