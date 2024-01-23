calc_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}")
    print("All good")

days_to_units(20)