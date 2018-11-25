print("AMNAH ZAREEN 18B-119-CS A")
print("PROGRAMMING EXERCISE LAB 5 QUESTION 5")
name = str(input("Enter your name :"))
f_name = str(input("Enter your Father's name :"))
group= str(input("Enter your group name :"))
total_marks = int(input("Enter the total marks :"))
roll_number = int(input("Enter your roll number :"))
def marksheet1(name, f_name, group, total_marks, roll_number):
    print("Your name is:", name)
    print("Your Father's name is :", f_name)
    print("Your group is:", group)
    print("The total marks are :", total_marks)
    print("Your roll number is:", roll_number)
sub_1 = eval(input("Enter the marks of chemistry :"))
sub_2 = eval(input("Enter the marks of Islamiat :"))
sub_3 = eval(input("Enter the marks of Physics :"))
sub_4 = eval(input("Enter the marks of Maths :"))
sub_5 = eval(input("Enter the marks of English :"))
sub_6 = eval(input("Enter the marks of Urdu :"))
marks_obtained  = int(input("Marks obtained out of :"))
def marksheet2(sub_1,sub_2,sub_3,sub_4,sub_5,marks_obtained):
    print("Marks of chemistry  :", sub_1)
    print("Marks of Islamiat  :", sub_2)
    print("Marks of Physics :", sub_3)
    print("Marks of Maths :", sub_4)
    print("Marks of English :", sub_5)
    print("Marks of Urdu :", sub_6)
    print("Marks obtained out of:", marks_obtained)    
obtained_marks = (sub_1 + sub_2 + sub_3 + sub_4 + sub_5 + sub_6) #FOR CALCULATING PERCENTAGE
percentage = (obtained_marks/total_marks)*100
if percentage  <= 90:
    print("GRADE A+")
    print("CONGRATULATIONS, YOU HAVE PASSED !!!")
elif percentage <= 80:
    print("GRADE A")
elif percentage  <= 70:
    print("GRADE B")
elif percentage  <= 60:
    print("GRADE C")
else:
    print("GRADE F")
marksheet1(name, f_name, group, total_marks,roll_number)
marksheet2(sub_1,sub_2,sub_3,sub_4,sub_5,marks_obtained)

    

    
