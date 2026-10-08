Homework = float(input("Enter your homework grade: "))
Quiz1 = float(input("Enter your first quiz grade: "))
Quiz2 = float(input("Enter your second quiz grade: "))
Quiz3 = float(input("Enter your third quiz grade: "))
Quizzes = (Quiz1 + Quiz2 + Quiz3) / 3
Midterm = float(input("Enter your midterm grade: "))
Final_Exam = float(input("Enter your final exam grade: "))
Participation = float(input("Enter your participation grade: "))

Homework_grade = Homework * 0.20
Quizzes_grade = Quizzes * 0.15
Midterm_grade = Midterm * 0.25
Final_Exam_grade = Final_Exam * 0.30
Participation_grade = Participation * 0.10

Final_Grade = (Homework_grade + Quizzes_grade + Midterm_grade + Final_Exam_grade + Participation_grade)

print("Your final grade is: " + str(Final_Grade))

if Final_Grade >= 90:
    print("Your final grade is an A.")
elif Final_Grade >= 80:
    print("Your final grade is a B.")
elif Final_Grade >= 70:
    print("Your final grade is a C.")
elif Final_Grade >= 60:
    print("Your final grade is a D.")
else:
    print("Your final grade is an F.")

    
    