# -*- coding: utf-8 -*-
"""
• Write a program that determine the tax rate based on two factors: 
salary and having kids or not:
    
If salary is in range of [30, 50] and the employee 
does not have kid tax is 40, if the salary is still in 
range of [30, 50] but the employee has kid tax is 
35. If salary in range of [50, 70] and the employee 
does not have kid tax is 50 if the salary is still in 
range of [50, 70] but the employee has kid then
tax is 45. If salary is less then 30 tax is 0 no matter 
if the employee has kid or not and if the salary is 
more then 70 the tax is 55 no matter if the 
employee has kid or not.
"""

"""
def bool_child():
    has_child = input("Do the employee have a child? True or False?")
    if has_child == "True":
        return True
    if has_child == "False":
        return False
bool_child()
"""
    
def tax_rate_calculator():
    
    has_child = input("Does the employee have a child? Yes or No?")
    if has_child == "Yes":
        has_child = True
    if has_child == "No":
        has_child = False
    
    salary = float(input("What is the employees yearly salary in thousands?"))
    
    
    if salary < 30:
        print("The tax rate is 0%")
        tax_rate = 0
        
    elif salary > 70:
        print("The tax rate is 55%")
        tax_rate = 55
        
    elif salary in range(30, 50) and not has_child:
        print("The tax rate is 40%")
        tax_rate = 40
    
    elif salary in range(30, 50) and has_child:
        print("The tax rate is 35%")
        tax_rate = 35
      
    elif salary in range(50, 70) and not has_child:
        print("The tax rate is 40%")
        tax_rate = 50
    
    elif salary in range(50, 70) and has_child:
        print("The tax rate is 35%")
        tax_rate = 45
        
    
    """
    Determine and display tax rate
    """
    print("The tax rate for this employee is", tax_rate)
    
    
    return
tax_rate_calculator()

