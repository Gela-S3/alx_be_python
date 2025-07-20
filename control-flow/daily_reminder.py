task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
if priority.lower() == "high":
    match time_bound.lower():
        case "yes":
            print(f"Reminder :{task} is {priority.lower()} priority task that requiers immediate attention today!")
        case "no":
            print(f"Reminder :{task} is {priority.lower()} priority task,but Complete it when you have free time.")
elif priority.lower() =="low":
    match time_bound.lower():
        case "yes":
            print(f"Reminder :{task} is {priority.lower()} priority task.Try to complete with in give time_bound")
        case "no" :
            print(f"Reminder :{task} is {priority.lower()} priority task.Consider completing it when you have free time.")
else:
    print("Please give a correct answer.")