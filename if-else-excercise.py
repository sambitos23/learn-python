import time

print("Today Day is", time.strftime("%a")+"day")
print("Current time is", time.strftime("%H:%M:%S"))
print(type(time.strftime("%H:%M:%S")))  # type string

hour = int(time.strftime("%H"))
min = int(time.strftime("%M"))
sec = int(time.strftime("%S"))

if 4 <= hour < 12 and min < 60 and sec < 60:  # 4:00:00 - 11:59:59
    print("Good morning")
elif hour <= 16 and min < 60 and sec < 60:
    print("Good afternoon")
elif hour < 20 and min < 60 and sec < 60:
    print("Good Evening")
else:
    print("Good night")
