import datetime

name = input("Please enter your name: ")

current_hour = datetime.datetime.now().hour

if 5 <= current_hour < 12:
    print("Good morning " + f"{name}!")
elif 12 <= current_hour < 18:
    print("Good afternoon " + f"{name}!")
else:
    print("Good evening " + f"{name}!")