class Student:

    def __init__(self, last_name, first_name,  age, average_score):

        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.average_score = float(average_score)

    def __str__(self):
        return f"Студент - {self.last_name} {self.first_name}. Вік - {self.age}. Середній бал - {self.average_score}"

    def change_average_score(self, value):
        self.average_score = float(value)

student_1 = Student("Поліщук", "Іван", 35, 5)
print(f"До зміну середнього балу: {student_1}")

student_1.change_average_score(9)

print(f"Після зміни середнього балу: {student_1}")