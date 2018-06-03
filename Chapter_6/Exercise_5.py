# Exercise 5: Take the following Python code that stores a string: str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float
# function to convert the extracted string into a floating point number.

# Original string
str = 'X-DSPAM-Confidence:0.8475'

# Find the index position of the 0
str.find('0')

# Convert the string from that point to the end of the string into a float.
float_number = float(str[19:])

# Print the float to ensure that the correct information has been sliced, and check the type to ensure it is a float.
print(float_number)
type(float_number)