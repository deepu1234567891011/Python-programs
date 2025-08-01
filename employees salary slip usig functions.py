def Employee_salary_slip(empname,emp_id,*salary,company='TCS'):
    total=sum(salary)
    average=total/len(salary)
    return empname,emp_id,company,total,average
result=Employee_salary_slip("srideepika",1234,30000,30000,30000,40000,5000)#storing return values in result variable
#unpack the return values
empname,emp_id,company,total,average=result
#print result
print("the employee name is:",empname)
print("the employee id is:",emp_id)
print("the employee comapny is:",company)
print("the employee total salary is:",total)
print("the employee average salary is:",average)