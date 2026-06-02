class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade
    
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        for value in grade:
            if value < 0 or value > 100:
                print("Invalid grade. Please enter a value between 0 and 100.")
                return
        self.__grade = grade
        print("Grade updated successfully.")
                
            
    def get_average(self):
        return sum(self.__grade) / len(self.__grade)

    def get_remarks(self):
        average = self.get_average()
        if average >= 90:
            return "Excellent"
        elif 75 <= average <= 89:
            return "Passed"
        else:
            return "Failed"
    
students = [
    Student("Juan", [-1, 90, 91, 89, 87]),
    Student("Pedro", [75, 80, 78, 82, 79])
]

students[0].set_grade([-1, 90, 91, 89, 87])
students[1].set_grade([75, 80, 78, 82, 79])