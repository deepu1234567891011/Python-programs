def student_details(studentname,Rollnumber,college,*marks):
    print("studentname is:",studentname)
    print("Rollnumber is:",Rollnumber)
    print("collagename is:",college)
    if len(marks)==0:
           print("cannot calculate")
           return
    total=sum(marks)
    average=total/len(marks)
    print("the  total is:",total)
    print("the average is:",average)
    if average>=80:
        grade='A'
    elif average>=60:
        grade='B'
    elif average>=40:
        grade='c'
    else:
        grade='fail try to next attempt'
    print("grade is:",grade)
student_details("srideepika",4461,"KLU",10,54,57,40)

          