class Student: 
    midterm = 0
    finalNote = 0 

    def __init__(self,name,surname,studentNumber):
        self.name=name
        self.surname=surname
        self.studentNumber= studentNumber
        print(f"Hoş Geldin {self.name} {self.surname} " )

    def gradeCalculation(self,midterm,finalNote):
        self.midterm=midterm
        self.finalNote=finalNote

        total = (midterm * 0.4) + (finalNote * 0.6)
        print(f"Ortalmanız: {total}")

#ogrenci = Student()
#ogrenci.gradeCalculation(38,68)