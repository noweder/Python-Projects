student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_heights = 0
count = 0
for height in student_heights:
    total_heights += height
    count += 1
average_height = round(total_heights / count)
print(average_height)
