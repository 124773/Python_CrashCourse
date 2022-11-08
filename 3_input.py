# input in Python
# Python uses the function input () to capture and store data
print("User Profile Application")

first_name = input ("First Name: ")
last_name = input ("Last Name: ")
occupation = input ("Your Job: ")

print ("Your First Name is " + first_name)
print ("Your Last Name is " + last_name)
print ("Your Occupation is " + occupation)

# Another way of outputting information in Python is through formatted strings
(f"Your First Name is {first_name} and your job is {occupation}")

# Handling Non-String input
age = int(input("Enter your age: "))

print(f"In two years, you will be {age+2} years old")