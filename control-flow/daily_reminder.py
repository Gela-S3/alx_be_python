task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
if time_bound.lower() == "yes":
    match priority.lower() :
        case "high":
            print(f"Reminder : {task} is {priority.lower()} priority task that requiers immediate attention today!")
        case "medium":
            print(f"Reminder : {task} is {priority.lower()} priority task,but complete it when you have free time.")
        case "low":
            print(f"Reminder : {task} is {priority.lower()} priority task.Try to complete with in give time_bound")
elif time_bound.lower() == "no":
    match priority.lower():
        case "high":
            print(f"Reminder : {task} is {priority.lower()} priority task.Give attention!")
        case "medium" :
            print(f"Reminder : {task} is {priority.lower()} priority task.Calm down! You have time to {task}")
        case "low" :
            print(f"Reminder : {task} is {priority.lower()} priority task.Consider completing it when you have free time.")
else:
    print("Please give a correct answer.")