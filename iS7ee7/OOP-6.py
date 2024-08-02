class Students:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Course:
    def __init__(self, course_name, max_score):
        self.course_name = course_name
        self.max_score = max_score
        self.students = []

    def add_students(self, student):
        if student.score >= self.max_score:
            self.students.append(student)

s1 = Students("mohamed", 91)
s2 = Students("khaled", 92)
s3 = Students("joe", 83)

c1 = Course("hacking", 90)

c1.add_students(s1)
print(c1.students[0].name)#todo => mohamed

c1.add_students(s2)
print(c1.students[1].name)#todo => khaled
print(c1.students[1].score)#todo => 92