my_friends = []
max_friends = 4


while max_friends > 0:

    friend = input("Add A Friend To The List: ")
    if friend.isupper():
        print("invalid name")

    elif friend.islower():
        my_friends.append(friend.capitalize().strip())
        max_friends -= 1
        print(f"Friend {friend} Added => 1st Letter Become Capital")

        print(f"Names Left in List Is {max_friends}")

    elif friend.istitle():
        my_friends.append(friend.capitalize().strip())
        max_friends -= 1
        print(f"Friend {friend} Added")
        print(f"Names Left in List Is {max_friends}")

else:
    print(my_friends)
