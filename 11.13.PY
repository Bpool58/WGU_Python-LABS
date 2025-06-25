#                                                  DICTIONARY METHODS


print("=== Dictionary Methods Demo ===")
student_grades = {'Alice': 95, 'Bob': 82, 'Charlie': 78}

def print_current_dict(dict_name, dictionary):
    print(f'\n{dict_name} currently contains:', dictionary)

print_current_dict('Student Grades', student_grades)

#   Demonstrate .get() with existing and non-existing keys
print("\n=== 1. Using .get() method ===")
print("Getting Bob's grade:", student_grades.get('Alice'))
print("Getting David's grade (doesn't exist):", student_grades.get('David', 'Not found'))

#           UPDATE THE DICTIONARY
print("\n=== 2. Using .update() method ===")
new_students = {'David': 63, 'Eve': 98}
print("adding new students:", new_students)
student_grades.update(new_students)
print_current_dict('adding new students', student_grades)

#           Demonstrating .pop() with existing and non existing keys

print("\n=== 3. Using .pop() method ===")
removed_grade = student_grades.pop('Bob')
print(f"\nRemoved Bob's grade: {removed_grade}")
print('trying to removed Frank (does not exist):', student_grades.pop('Frank', 'Not found'))
print_current_dict('Student Grades', student_grades)

#               DEMONSTRATING CLEAR
print('\n=== 4. using .clear() method ===')
print('Clearing all grades...')
student_grades.clear()
print_current_dict('Student Grades', student_grades)


print("\n=== Demo Complete ===")
