# Question 1 - Student Result System

students = [
    {"name": "Aarav", "marks": {"Math": 85, "Science": 78, "English": 92}},
    {"name": "Sita", "marks": {"Math": 90, "Science": 88, "English": 79}},
    {"name": "Ram", "marks": {"Math": 67, "Science": None, "English": 74}},
    {"name": "Gita", "marks": {"Math": 72, "Science": 81}},
    {"name": "Hari", "marks": {"Math": 95, "Science": 91, "English": 89}},
]

SUBJECTS = ["Math", "Science", "English"]
MAX_MARKS_PER_SUBJECT = 100


def find_student(name):
    """Return the student dictionary, or raise KeyError if not found."""
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    raise KeyError(name)


def calculate_total(marks):
    """Add up the marks. A missing mark is counted as 0."""
    total = 0
    for subject in SUBJECTS:
        try:
            total += marks[subject]
        except (KeyError, TypeError):
            print(f"Warning: {subject} mark is missing. It is counted as 0.")
    return total


def calculate_percentage(total):
    """Return the percentage out of the full marks for all subjects."""
    full_marks = len(SUBJECTS) * MAX_MARKS_PER_SUBJECT
    return (total / full_marks) * 100


name = input("Enter student name: ").strip()

try:
    student = find_student(name)
    total = calculate_total(student["marks"])
    percentage = calculate_percentage(total)
    print(f"\nResult for {student['name']}")
    print(f"Total Marks : {total} / {len(SUBJECTS) * MAX_MARKS_PER_SUBJECT}")
    print(f"Percentage  : {percentage:.2f}%")
except KeyError:
    print(f"Error: Student '{name}' does not exist.")
