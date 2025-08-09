print("***Student Information")

student_name = input("Enter Your Name -> ")
student_roll_no = int(input("Enter Your rollno -> "))
subject_python_marks = float(input("Enter Marks python -> "))
subject_django_marks = float(input("Enter Marks of django -> "))
subject_database_marks = float(input("Enter marks of database -> "))

total = subject_python_marks+subject_django_marks+subject_database_marks
percentage = total/3

print()
print("*"*22)
print("Student Name -> ",student_name)
print("Student Roll No -> ",student_roll_no)
print("Total Subject Marks -> ",total)
print("Percentage -> ",percentage)
print("*"*22)

if percentage >= 90:
    print("Congratulations For *A+*")

elif percentage >= 70:
    print("A")

elif percentage >= 60:
    print("B")

elif percentage >= 50:
    print("C")

else:
    print("So sorry, you just failed.")

