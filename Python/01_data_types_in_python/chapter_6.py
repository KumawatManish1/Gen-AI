#Strings
##Strings are immutable sequences of characters.
##Strings are defined using single or double quotes.
##Strings are indexed by character.
##Strings are iterable.



chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")



#String Indexing
#String indexing is the process of accessing a single character in a string.
#String indexing starts at 0.
#String indexing ends at the length of the string - 1.
#String indexing is accessed using square brackets [].
#String indexing has start and end index.
#String indexing has step index.

chai_description = "Aromatic and bold"

print(chai_description[0:8])
print(chai_description[:8])
print(chai_description[13:]) 
print(chai_description[::2])
print(chai_description[::-1])



#encoding and decoding
#encoding is the process of converting a string to a sequence of bytes. 
label_text = "Chai Spécial"
encoded_text = label_text.encode("utf-8")
print(f"Non encoded text: {label_text}")
print(f"Encoded text: {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"Decoded text: {decoded_text}") 