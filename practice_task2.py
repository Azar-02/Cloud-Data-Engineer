# Write a program that reads a list of students and their marks from a dictionary, then:
# Prints total and average marks
# Identifies who scored above 90

# Sample dictionary of students and their marks
students = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 91,
    "David": 76,
    "Eve": 88,
    "Frank": 93
}

# 1. Calculate total and average marks
total_marks = sum(students.values())
average_marks = total_marks / len(students)

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")

# 2. Identify students who scored above 90
print("\nStudents who scored above 90:")
for name, marks in students.items():
    if marks > 90:
        print(f"- {name} ({marks})")
