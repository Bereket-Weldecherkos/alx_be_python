task = input("What is your task for today? ")
priority = input("What is the priority of this task? (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task that requires attention today.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed soon.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. You can complete it after the high priority tasks.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task, but it should be completed soon.")
        else:
            print(f"Note: '{task}' is of low priority. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")