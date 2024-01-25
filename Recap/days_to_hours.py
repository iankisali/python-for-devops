calc_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
   return f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}"

def validate_execute():
   try:
     user_num = int(user_input)
     if user_num > 0:
        calc_value = days_to_units(user_num)
        print(calc_value)
     elif user_num == 0:
        print ("You entered zero!!!")
     else:
        print ('Entered negative number!!')
     
   except ValueError:
      print("Invalid value!!")

user_input = input("Enter hours to convert to days!\n")
validate_execute()