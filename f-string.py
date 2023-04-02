# Old format
letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Harry"

print(letter.format(name, country))

txt = "For only {price:.2f} dollars"  # we use .2f when we need only 2 value of a float number
print(txt.format(price=49))


# New format as f-string
print(f"We use f-string like this: Hey my name is {{name}} and I am from {{country}}")
print(f"Hey my name is {name} and I am from {country}")
price = 49.09999
print(f"For only {price:.2f} dollars")
print(f"{2*30}")
print(type(f"{2*30}"))
