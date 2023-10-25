marks = []

num_students = int(input("Enter the number of students: "))
num_subjects = 5

for i in range(num_students):
    print(f"Enter marks for student {i + 1}:")
    student_marks = []
    for j in range(num_subjects):
        mark = int(input(f"Subject {j + 1}: "))
        student_marks.append(mark)
    marks.append(student_marks)

totals = [sum(student) for student in marks]

subject_totals = [sum(marks[i][j] for i in range(num_students)) for j in range(num_subjects)]
subject_averages = [total / num_students for total in subject_totals]

print("Total marks of each student:", totals)
print("Average marks in each subject:", subject_averages)
