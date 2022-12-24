student_heights = input('Input a list of student heights ').split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# total_height = 0
# total_students = 0

# for student_height in student_heights:
#     total_height += student_height
#     total_students += 1

# average_student_height = round(total_height / total_students)

total_height = sum(student_heights)
total_students = len(student_heights)
average_student_height = round(total_height / total_students)

print(average_student_height)