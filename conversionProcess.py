# Imports conversion chart from conversionData.py
from conversionData import conversion_code

# Takes input from user
userInp = input("Type the message: \n")




# Creating converted output
converted_data = ""


for i in range(0, len(userInp)):
    if userInp[i] in conversion_code.keys():
        # Replaces each of the letters (keys) with a value from the conversion chart by iterating through the message.
        converted_data += conversion_code[userInp[i]]
        
    else:
        converted_data += userInp[i]

print("Secret Message: ", converted_data)

