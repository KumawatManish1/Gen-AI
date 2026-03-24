#Tuples
##Tuples are immutable sequences of objects.
##Tuples are defined using parentheses.
##Tuples are indexed by object.
##Tuples are iterable. 


spices = ("cumin", "coriander", "cinnamon")

(spice1, spice2, spice3) = spices

print(f"Main Spices : {spice1}, {spice2}, {spice3}")

ginger_ratio , cloves_ratio = 4, 2
print(f"Ginger ratio: {ginger_ratio} and Cloves ratio: {cloves_ratio}")
ginger_ratio, cloves_ratio = cloves_ratio, ginger_ratio
print(f"Ginger ratio: {ginger_ratio} and Cloves ratio: {cloves_ratio}") 

#membership test

print(f"is cardamum in spices? {'cardamum' in spices}")
print(f"is  in spices? {'cardamum' in spices}")
