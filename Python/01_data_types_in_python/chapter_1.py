# Object and Mutability

# Object:
## Everything in Python is an object.
## Objects have identity, Type and Value.
## Objects can be mutable or immutable.

# Mutable and Immutable Objects:
## Mutable Objects are those that can be changed after they are created.
## Immutable Objects are those that cannot be changed after they are created.
## Identity helps us to identify if objects are mutable or immutable.
## never check mutability usibg value, always check identity.

#THE CONCEPT OF MUTABILITY AND IMMUTABILITY IS WHAT VALUE WE CAN CHANGE IN THE MEMORY ITSELF.

sugar_amount = 2
print(f"Initial sugar:{sugar_amount}")

sugar_amount = 12
print(f"Second Intial sugar:{sugar_amount}")

print(f"ID of 2 is {id(2)}")
print(f"ID of 12 is {id(12)}")

# sugar_amount is the refernce which points to the object 2(assigned in the memory), similarily for 12.so, the values does not change(immutable), but the reference changes(mutable).