print('PROGRAMMING EXERCISE QUESTION -4')
name=str(input('Enter your Name :'))
f_name=str(input('Enter your Father name :'))
group=str(input('Enter your Group Name :'))
total_marks=int(input('Enter the total marks :'))


subject1=eval(input('Enter the marks of chemistry :'))
subject2=eval(input('Enter the marks of islamiyat :'))
subject3=eval(input('Enter the marks of maths :'))
subject4=eval(input('Enter the marks of physics :'))
subject5=eval(input('Enter the marks of english  :'))
subject6=eval(input('Enter the marks of urdu  :'))
#FOR CALCULATING PERCENTAGE
obtained_marks=(subject1+subject2+subject3+subject4+subject5+subject6)
percentage=(obtained_marks/total_marks)*100
if percentage <=90:
    print('GRADE A+')
elif percentage <=80:
    print('GRADE A')
elif percentage <=70:
    print('GRADE B')
elif percentage <=60:
    print('GRADE C')
else:
    print('GRADE F')

print('Name is' + ' ' + name)
print('Father name is' + ' ' + f_name)
print('Student marks obtained in all subjects are' + ' ' + str(obtained_marks))
print('Total marks are' , total_marks)
print('Group name is', group)
print('Student percentage is ',  percentage)
print('Your grade is A+')
print('CONGRATULATIONS!!')
              
