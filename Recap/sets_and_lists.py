month_set = {"Jan", "Feb", "March"}
for month in month_set:
    print(month)

month_set.add("April")
print(month_set)
month_set.remove("Jan")
print(month_set)

month_list = ["Jan", "Feb", "March"]
print(month_list)
print(type(month_list))
print(month_list[-1])

my_dictionary = {"days": 20, "unit": "hours", "message": "all good"}
print(my_dictionary["days"])
print(my_dictionary["hours"])