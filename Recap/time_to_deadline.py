import datetime

user_date = input("Enter your goal with deadline: \n")
input_list = user_date.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

#Calculation

today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(f"Time remaining for your goal {goal} is {time_till.days} days")