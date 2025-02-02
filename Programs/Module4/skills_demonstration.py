user_grade = float(input("What is your current total grade?: "))

if user_grade >= 96:
    print("You will get a GPA of 4.0")
elif user_grade >= 93:
    print("You will get a GPA of 3.7")
elif user_grade >= 90:
    print("You will get a GPA of 3.3")
elif user_grade >= 87:
    print("You will get a GPA of 3.0")
elif user_grade >= 83:
    print("You will get a GPA of 2.7")
elif user_grade >= 80:
    print("You will get a GPA of 2.3")
elif user_grade >= 77:
    print("You will get a GPA of 2.0")
elif user_grade >= 73:
    print("You will get a GPA of 1.7")
elif user_grade >= 70:
    print("You will get a GPA of 1.3")
elif user_grade >= 67:
    print("You will get a GPA of 1.0")
elif user_grade >= 63:
    print("You will get a GPA of 0.7")
else:
    print("Sorry, but you're going to fail.")
