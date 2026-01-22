class student:
	def __init__(self, student_grade, student_name):
		self.name = student_name
		self.grade = student_grade


student_1 = student('ashish', 10)
print(f"the name of the student is : {student_1.name} and he is studying in class : {student_1.grade}")
