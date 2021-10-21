# -*- coding: utf-8 -*-
"""
Programming for Data Analytics Lab 1

"""



"""
Using Python in interactive mode:
a) Print:
I like “Python”
b) Print:
I like ‘Python’
c) Create a String variable to store your name and an int variable to store your age. 
Using a single print statement print this information to the screen
"""

def Q1():
    
    print("I like \"Python\"")
    print("I like \'Python\'")
    
    name = 'Daniel'
    age = 24
    
    print(name,age)
    return

Q1()



"""
Use Python in Script Mode:
a) Using script mode write a program that will output the text Hello ‘Python’
and in the next line Hello “Python”
b) Create a String variable to store your name in an int variable to store your age. 
Print this out to screen using the Script mode.
"""

def Q2():
    
    return
Q2()



"""
Write a program that asks the user to enter a distance in kilometres and then converts that 
distance to miles (Miles = Kilometres * 0.6214) and prints it like this: The distance is XXX 
miles.
"""

def Q3():
    
    dist = int(input("Enter a distance in kilometres"))
    miles = dist * 0.6214
    print(" The distance is", miles , "miles.")
    
    return
Q3()



"""
Write a program that will ask a student for their first name and then for their surname. It should 
then ask the student to enter the int numerical grade they received in each of their three subjects. 
The program should then print out the full name of the student along with their average 
numerical grade (Use only a single print statement)
"""

def Q4():
    f_name = input("Enter your first name:")
    s_name = input("Enter your surname:")
    
    grade_subject_1 = int(input("Enter the result obtained in your first subject"))
    grade_subject_2 = int(input("Enter the result obtained in your second subject"))
    grade_subject_3 = int(input("Enter the result obtained in your third subject"))
    
    print("Student name : ", f_name , s_name , 
          "Student average grade : ", (grade_subject_1 , grade_subject_2 , grade_subject_3)/3)
    
    return
Q4()



"""
Write a program to calculate and display a person’s body mass index (BMI). A persons BMI is 
calculated with the following formula: 
BMI = (weight/ height^2 ) * 703
Where weight is in pounds and height is in inches. Your program should ask the user for their
weight (in pounds) and height (in inches). 
"""

def Q5():
    weight = float(input("Enter your weight (in pounds) : "))
    height = float(input("Enter your height (in inches) : "))
    
    BMI = (weight / height * height) * 703
    print("Your BMI is " , BMI)
    return
Q5()



"""
There are three seating categories at a stadium. For a football games, Class A seat’s cost €25, 
Class B seat’s cost €20 and Class C seat’s cost €30. Write a program that asks how many tickets 
for each class of seats were sold, and then display the amount of income generated from ticket 
sales. 
"""    

def Q6():
    A_price = 25
    B_price = 20
    C_price = 30
    
    A_sold = int(input("How many seat A tickets were sold?"))
    B_sold = int(input("How many seat B tickets were sold?"))
    C_sold = int(input("How many seat C tickets were sold?"))
    
    income = (A_price*A_sold) + (B_price*B_sold) + (C_price*C_sold) 
    print("Total income = €" , income)
    return
Q6()




"""   
Write a program that asks the user to enter his/her name and age in year and then calculate the 
number of months and days and prints the results as follows:
Enter your name: Farshad
Enter your age: 98
Farshad is 1176 months old
Farshad is 35770 days old
"""

def Q7():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    months = age*12
    days = age*365
    
    print(name, "is ", months, " months old ")
    print(name, "is ", days, " days old ")
    return
Q7()    




"""
Write a program that asks the user to enter radius of a circle and then calculate the area of the 
circle using the following formula: area = pie r^2 where pie = 3.14 and r is the radius, then print 
the value of the area and also prints the type of the variable area.
Note: The user is allowed to enter either int or float value.
"""

def Q8():
    r = float(input("Enter the radius of a circle"))
    area = 3.14*(r*r)
    
    print("The area of the circle is: ", area)
    return
Q8()
    
    
    