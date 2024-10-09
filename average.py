
grades = []
for i in range(3):
    grade = int(input("Input grade: "))
    grades.append(grade)

sum = 0
for _ in grades:
    sum+= _

average,status = sum/3, "Passing" if sum/3 >= 60 else "Failing"


print(f"{average:.2f}%, {status}")
