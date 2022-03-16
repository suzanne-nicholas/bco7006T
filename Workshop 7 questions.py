australian_states = {
    "VIC": "Victoria",
    "NSW": "New South Wales",
    "QLD": "Queensland",
    "WA": "Western Australia",
    "NT": "Northern Territory",
    "SA": "South Australia",
    "ACT": "Australian Capital Territory",
    "TAS": "Tasmania"
,}

#use loops
print("\n \n")
for i in australian_states:
    print("State abbreviation is", i)
    print("the full name is", australian_states[i])

print("\n \n")

hello = "great day"

try:
    print(x)
except NameError:
    print("Go back and assign your x!")
#finally:
else:
    print("the 'try except' is finished")


try:
    print(hello)
except:
    print("Something went wrong")
else:
    print("Everything went great")

x=11

if x == 10:
    raise Exception("you cannot use 10, only one digit numbers please")

if x<20:
    raise Exception("your x is less than 20")


