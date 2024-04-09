#1
grades=[85,90,95,89,78,88,76,80,72,93]
grades.sort(reverse=True)
def Average(grades):
    return sum(grades)/ len(grades)
grades=[85,90,95,89,78,88,76,80,72,93]
grades= Average(grades)
print(grades)

#2
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
commmon_names=list(set(submitted)and set(attended))
print(commmon_names)
if submitted==attended:
    print("These lists are identical")
else:
    print("These lists are different")
    
left_over=list(set(attended).difference(submitted))
print(left_over)

#3
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
new_temp=slice(temperatures[7:14])
print(new_temp)
over_hundred=slice(temperatures[24:])
print(over_hundred)
temperatures.reverse()
print(temperatures)
print(temperatures[6:11])

#4
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

filtered_student=students[2]+str(grades[2])+activities[2]
print(filtered_student)
students_approved=["John","Doe","Smith"]
print(students_approved)


