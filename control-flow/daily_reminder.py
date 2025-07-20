task = input("Enter your task: ").strip()
if not task:
    print("Task description cannot be empty.")
    exit()

# Priority input
priority = input("Enter the task priority (high, medium, low): ").strip().lower()
if priority not in ["high", "medium", "low"]:
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
    exit()

# Time-bound input
time_bound = input("Is this task time-bound? (yes/no): ").strip().lower()
if time_bound not in ["yes", "no"]:
    print("Please enter 'yes' or 'no' for time-bound.")
    exit()

# Match case for priority
match priority:
    case "high":
        print(f"🔔 High priority task: '{task}'")
    case "medium":
        print(f"📌 Medium priority task: '{task}'")
    case "low":
        print(f"📝 Low priority task: '{task}'")

# Time-sensitive check
if time_bound == "yes":
    print("This task requires immediate attention today!")
