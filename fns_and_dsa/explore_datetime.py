# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date  # return so it can be reused

def calculate_future_date(current_date, days_to_add):
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format as "YYYY-MM-DD"
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)

def main():
    # Part 1: Show current date/time
    current_date = display_current_datetime()

    # Part 2: Ask user for number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
