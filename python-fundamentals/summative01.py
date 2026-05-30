student_grade = [
    {"name": "Daynx", "grade": [90, 85, 92, 92, 94]},
    {"name": "Juan", "grade": [88, 90, 91, 89, 87]},
    {"name": "Maria", "grade": [75, 80, 78, 82, 79]},
    {"name": "Pedro", "grade": [95, 92, 96, 94, 98]}
]

def get_average (student_grade):
    total = sum(student_grade["grade"])
    average = total / len(student_grade["grade"])
    return average

def get_remarks (average):
    if average >= 90:
        return "Excellent"
    elif 75 <= average < 90:
        return "Passed"
    else:
        return "Failed"

for student in student_grade:
    average = get_average(student)
    remarks = get_remarks(average)
    print(f"Name: {student['name']} | Average: {average:.2f} | Remarks: {remarks}")