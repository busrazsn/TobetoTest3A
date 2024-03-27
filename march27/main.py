from student import Student 
from teacherList import Teacher

name=input("Adinizi Girin: ")
surname= input("Soyadinizi Girin: ")
studentNumber=input("Ogrenci numaranizi girin: ")

student=Student(name,surname,studentNumber)
student.gradeCalculation(38,68)
student.name = name

teacher1 = Teacher()
print(teacher1.teacherList)