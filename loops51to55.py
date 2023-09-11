# my_nums = [15, 81, 5, 17, 20, 21, 13]
# a = 0
# my_nums.sort(reverse=True)
# for num in my_nums:
# if num % 5 == 0:
#    a += 1
#    print(f"{a} => {num}")
# print("all numbers are printed")


# for x in range(1, 21):
#  if x == 6 or x == 8 or x == 12:
#     continue
# else:
#     print(str(x).zfill(2))

# print("All Numbers Are Printed")


my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

points = {
    'A': 100,
    'B': 80,
    'C': 40

}
total_points = 0
for rank in my_ranks:
    print(f"My Rank in {rank} Is {my_ranks[rank]} And This Equal {points[my_ranks[rank]]} ")
    total_points += points[my_ranks[rank]]

print(f"Total Points Is {total_points}")
