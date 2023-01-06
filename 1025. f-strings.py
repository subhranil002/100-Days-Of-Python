letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Subhranil"
print(letter.format(name, country))
# Hey my name is Subhranil and I am from India
print(letter.format(country, name))
# Hey my name is India and I am from Subhranil

letter = "Hey my name is {1} and I am from {0}"
print(letter.format(country, name))
# Hey my name is Subhranil and I am from India

letter = f"Hey my name is {name} and I am from {country}" # Introducing F-STRING
# Hey my name is Subhranil and I am from India

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.123456789)) # For only 49.12 dollars!

price = 49.123456789
txt = f"For only {price:.2f} dollars!"
print(txt) # For only 49.12 dollars!
# print(txt.format(price = 49.123456789)) # For only 49.12 dollars!