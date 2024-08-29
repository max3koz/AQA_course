from lesson_l14.Student import Student

student_1: Student = Student("Mark", "Twen", 67, 10.1)

print(f"The students name is {student_1.name}")
print(f"The students surname is {student_1.surname}")
print(f"The students age is {student_1.age}")
print(f"The students average mark is {student_1.avd_mark}\n")

student_1.change_avd_mark(new_avd_mark=9)
print(f"The average mark really was changed to {student_1.avd_mark}")
