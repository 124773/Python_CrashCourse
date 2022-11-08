# Python uses 'if' statements to evaluate conditions
driver_age = int(input ("Please Enter Your Age: ")) 

if (driver_age >= 18):
    print ("Eligible to have a driver's license")
else:
    print ("Not Eligible ")
    print(f"Please Check back with us in {18 - driver_age} years")