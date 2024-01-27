calc_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
   return f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}"

def validate_execute():
   try:
     user_num = int(days)
     if user_num > 0:
        calc_value = days_to_units(user_num)
        print(calc_value)
     elif user_num == 0:
        print ("You entered zero!!!")
     else:
        print ('Entered negative number!!')
     
   except ValueError:
      print("Invalid value!!")

user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days !\n")
    list_of_days = user_input.split(", ")
    print(type(set(list_of_days)))
    for days in set(list_of_days):
        validate_execute()