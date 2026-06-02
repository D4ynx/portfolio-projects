class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def get_average(self):
        return sum(self.grade) / len(self.grade)

    def get_remarks(self):
        average = self.get_average()
        if average >= 90:
            return "Excellent"
        elif 75 <= average <= 89:
            return "Passed"
        else:
            return "Failed"
        
class GraduateStudent(Student):
    def __init__ (self, name, grade, thesis_title):
        super().__init__(name, grade)
        self.thesis_title = thesis_title
        
    def get_remarks(self):
        average = self.get_average()
        if average >= 90:
            return "Distinction"
        elif 75 <= average <= 89:
            return "Passed"
        else:
            return "Failed"

students = [
    Student("Juan", [88, 90, 91, 89, 87]),
    Student("Pedro", [75, 80, 78, 82, 79])
]

graduate_students = [
    GraduateStudent("Daynx", [90, 85, 92, 92, 94], "Impact of AI on Society"),
    GraduateStudent("Maria", [75, 80, 78, 82, 79], "Effects of Climate Change")
]

for student in students:
    print(f"Name: {student.name} | Average: {student.get_average():.2f} | Remarks: {student.get_remarks()}")

for grad_student in graduate_students:
    print(f"Name: {grad_student.name} | Average: {grad_student.get_average():.2f} | Remarks: {grad_student.get_remarks()} | Thesis Title: {grad_student.thesis_title}")