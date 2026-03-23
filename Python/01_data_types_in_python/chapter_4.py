#Numbers
##Integers
##Floating Point Numbers -> decimal numbers
##Boolean -> True or False
##Real Numbers -> 1.23, 1.23e-10
##Complex Numbers -> 2 +3j

is_boiling = True
stri_count = 5
total_action = is_boiling + stri_count  # upcasting the boolean to integer
print(f"Total action is {total_action}")

milk_present = 0 # downcasting the integer to boolean
print(f"Is there milk? {bool(milk_present)}")

#Logical Operators: and, or, not
##and_result = True and True
##or_result = True or False
##not_result = not True