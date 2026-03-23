spice_mix = set()
print(f"initial spice mix: {id(spice_mix)}")
print(f"spice mix: {spice_mix}")

spice_mix.add("cumin")
spice_mix.add("ginger")

print(f"After spice mix: {id(spice_mix)}")
print(f"spice mix: {spice_mix}")

#output:
#initial spice mix: 1567715926176
#After spice mix: 1567715926176

#as we can see from the output, the id of the spice mix does not change, even though we added more items to it. This is because the SET IS MUTABLE, and the id of the set does not change.

#THE CONCEPT OF MUTABILITY AND IMMUTABILITY IS WHAT VALUE WE CAN CHANGE IN THE MEMORY ITSELF.