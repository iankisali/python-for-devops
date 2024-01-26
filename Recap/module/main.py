from hepler import validate_execute, user_input_msg

user_input = ""
while user_input != "exit":
    user_input = input(user_input_msg)
    days_and_units = user_input.split(":")
    print(days_and_units)
    my_dict = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(my_dict)
    print(type(my_dict))
    validate_execute(my_dict)
