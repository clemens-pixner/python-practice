
workout = []
counter = 0

print("Workout Tracker")

menu = """
-----------------------
1) Add Workout 
2) View Workout 
3) Exit Workout Tracker
-----------------------
"""
print(menu)


while True:
    try:
        selection = int(input("What do you want to do (1/2/3)? "))
    except ValueError:
        print("Please enter 1, 2 or 3")
    
    if selection == 1:
        amount = int(input("How much exercises did you do?"))
        for i in range(amount):
            name = str(input("What exercise did you do? "))
            reps = int(input("How many reps did you do? "))
            weight = float(input("With how much weight? "))
            total_weight = reps * weight

            exercise = {
                "name" : name,
                "reps" : reps,
                "weight" : weight
            }

            workout.append(exercise)
            print("Workout added")

    elif selection == 2:
        if len(workout) == 0:
            print("No Workout found")
            continue
        else:
            for ex in workout:
                print(f"\nExercise: {ex['name']}")
                print(f"Reps: {ex['reps']}")
                print(f"Weight: {ex['weight']}Kg")
                print(f"Total weight: {ex['reps'] * ex['weight']}Kg")
    else:
        print("Goodbye!")
        break
