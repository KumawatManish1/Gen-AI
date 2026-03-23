#Numbers
##Integers
##Floating Point Numbers -> decimal numbers
##Boolean -> True or False
##Real Numbers -> 1.23, 1.23e-10
##Complex Numbers -> 2 +3j

# Integer:
black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Remaining tea is {remaining_tea}")

milk_litres = 7
serving = 4
milk_per_serving = milk_litres / serving
print(f"Milk per serving is {milk_per_serving}")

tea_bags = 7
pots = 4
tea_bags_per_pot = tea_bags // pots
print(f"Tea per pot is {tea_bags_per_pot}")
# // is used to get the integer part of the division. It is called floor division. 

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover pods are {leftover_pods}")
# % is used to get the remainder of the division. It is called modulo.

base = 2
power = 3
result = base ** power
print(f"{base} to the power of {power} is {result}")
# ** is used to get the power of the base. It is called exponentiation.

total_tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested is {total_tea_leaves_harvested}")
# _ is used to make the number more readable. It is called underscore.