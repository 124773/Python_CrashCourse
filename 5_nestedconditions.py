student_mark = int(input("Enter Final Mark: "))

if(student_mark >= 70):
    print("Pass: Grade A")
    elif (student_mark >= 60):
        print("Pass: Grade B")
        elif (student_mark >= 50):
            print("Pass: Grade C")
            elif (student_mark >= 40):
            print("Pass: Grade D")
else:
    print("Fail")