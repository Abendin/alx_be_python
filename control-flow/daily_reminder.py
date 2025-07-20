task = input("Enter your task: ")
priority = input("Enter the task priority (high, medium, low): ").strip().lower()
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()


match priority:
    case "high":
        print(f"High priority task: '{task}'")
    case "medium":
        print(f"Medium priority task: '{task}'")
    case "low":
        print(f"Low priority task: '{task}'")
    case _:
        print(f"Unknown priority level for task: '{task}'")

if time_bound == "yes":
    print("This task requires immediate attention today!")
