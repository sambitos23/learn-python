# Strings are immutable

a = "Sambit"
print(len(a))

# string method doesn't change the existing sting, it will  return new string
print(a.upper())
print(a.lower())

b = "!!!Sambit!!!"
print(b.rstrip("!"))  # it does not remove the leading characters
print(a.replace("Sambit", "Harry"))

str2 = "hello world"
print(str.split(" "))

blogHeading = "intro tO Js"
print(blogHeading.capitalize())

c = "sambit harry !!! sambit!"
print(c.count("sambit"))
print(c.endswith("!"))
print(c.endswith("!", 4, 16))

print(c.find("h"))  # first occurrence of str
print(c.index("!"))  # if it is not true index will throw an error (ValueError: substring not found)

str1 = "WelcomeToConsole22"
print(str1.isalnum())
print(str1.isalpha())
print(str1.islower())

str1 = "World health Organization"
print(str1.istitle())
print(str1.title())
