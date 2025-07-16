# Ask the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Build the main part of the message using match-case
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unrecognized priority level"

# Append time sensitivity note
if time_bound == "yes":
    message = "Reminder: " + message + " that requires immediate attention today!"
else:
    message = "Note: " + message + ". Consider completing it when you have free time."

# Final print
print(message)
