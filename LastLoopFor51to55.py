students = {
    "Ahmed": {
        "Math": "A",
        "Science": "D",
        "Draw": "B",
        "Sports": "C",
        "Thinking": "A"
    },
    "Sayed": {
        "Math": "B",
        "Science": "B",
        "Draw": "B",
        "Sports": "D",
        "Thinking": "A"
    },
    "Mahmoud": {
        "Math": "D",
        "Science": "A",
        "Draw": "A",
        "Sports": "B",
        "Thinking": "B"
    }
}

points = {
    'A': 100,
    'B': 80,
    'C': 40,
    'D': 20

}
total_point = 0
for key, values in students.items():
    total_point = 0
    print("-" * 30)
    print(f"-- Student Name => {key}")
    print("-" * 30)
    for child_key, child_value in values.items():
        print(f"- {child_key} => {points[students[key][child_key]]}")
        total_point += points[students[key][child_key]]
    print(f"Total Points For {key} Is {total_point}")
