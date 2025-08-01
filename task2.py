s_name=str.upper(input("Enter Student's Fullname:-"))
maths=int(input("Enter marks maths:-"))
science=int(input("Enter marks science:-"))
computer=int(input("Enter marks computer:-"))
socialscience=int(input("Enter marks socialscience:-"))
print(s_name)
total_marks=400
marks = maths+science+computer+socialscience
print(marks)
per=( marks/4)
print(per)
# print("hello",s_name,"you scored",marks,"in Exam")
if marks > 400:
     print("Restart")
else:
     print("continue")

if per >= 90 :
    grade = 'A+'
elif per >= 80:
    grade = 'A'
elif per >= 70:
    grade = 'B'
elif per >= 60:
    grade ='c'
elif per >= 50:
    grade = 'D'
else:
    grade = 'E'

print(f"Hello {s_name} your Grade: {grade}")
        












# if marks  > 400:
#     print(marks)
#     if per >=90 and per <=100:
#         print("Hello",s_name,"you Scored Grade A+ you obtain",marks,"in exam")
#     elif per >=80 and per <=70:
#         print("Hello",s_name,"you Scored Grade A you obtain",marks,"in exam")
#     elif per >=70 and per <=60:
#         print("Hello",s_name,"you Scored Grade B you obtain",marks,"in exam")
#     elif per >=60 and per <=50:
#         print("Hello",s_name,"you Scored Grade C you obtain",marks,"in exam") 
#     elif per >=50 and per <=40:
#         print("Hello",s_name,"you Scored Grade D you obtain",marks,"in exam")    
#     else: print("Enter valid marks")
# else: print("Try again ")
