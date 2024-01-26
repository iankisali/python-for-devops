def days_to_units(num_of_days, conversion_unit):
   if conversion_unit == "hours":
    return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
   elif conversion_unit == "minutes":
      return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
   else:
      return "Unsupported unit"

def validate_execute():
   try:
     user_num = int(my_dict["days"])
     if user_num > 0:
        calc_value = days_to_units(user_num, my_dict["unit"])
        print(calc_value)
     elif user_num == 0:
        print ("You entered zero!!!")
     else:
        print ('Entered negative number!!')
     
   except ValueError:
      print("Invalid value!!")

user_input = ""
while user_input != "exit":
    user_input = input("Enter number of days and conversion unit\n")
    days_and_units = user_input.split(":")
    print(days_and_units)
    my_dict = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(my_dict)
    print(type(my_dict))
    validate_execute()

