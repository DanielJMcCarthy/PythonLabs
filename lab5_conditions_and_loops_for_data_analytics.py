


"""
(1)
(Basic if/elif statements)
The area of a rectangle is the length multiplied by width. Write a program that asks for the 
length and width of two rectangles. The program should tell the user which rectangle has the 
greater area or if the areas are the same. 
"""

def Q1():

    
    length = float(input("What is the length of rectangle A?"))
    width = float(input("What is the width of rectangle A?"))
    
    area_A = length * width
    
    print("Area A =", area_A)
    
    
    length = float(input("What is the length of rectangle B?"))
    width = float(input("What is the width of rectangle B?"))
    
    area_B = length*width
    
    print("Area B =", area_B)
  
    
    
    if area_A > area_B:
        print("Rectangle A has a greater area")
        
    elif area_B > area_A:
        print("Rectangle B has a greater area")
        
    else:
        print("The rectangles have the same area")

Q1()




"""
Write a program that will use nested if statements to determine if a user is 
sufficiently qualified to be employed. The first if statement should check if the 
user has 4 years of commercial software development experience, the second 
nested if statement should check if they have a Microsoft certification and the 
final nested if statement should check if the user has a first class honours 
undergraduate computing degree.

If the user does not satisfy one of the conditions the program should inform the 
user that they are not eligible and should also inform the user of the requirement 
they have failed. The program should then exit.
"""

def Q2i():

    years_experience = int(input("How many years of software experience do you have?" ))
    
    if years_experience >=4:
        
        
        micro_cert = input("Do you have a microsoft certificate Y/N?")
        
        if micro_cert == "Y":
            
            
            degree = input("Do you have a first class honours undergraduate computing degree Y/N?")
            
            if degree == "Y":
                
                
                print("You are eligible")
                
            else :
                
                print("You do not have the valid requirement (honours degree)")
        
        else :
            print("You do not have the valid requirement (microsoft certificate)")
                
    else :
        print("You do not have the valid requirement (4+ years experience)")
                
            
    
    
    #if (years_experience < 4 or micro_cert == "N" or degree == "N"):
        
       # print("You do not have the valid requirements ")
        
       # else
        
      #      print("You are eligible")

Q2i()

"""
Rewrite the above program so you only use only a single if statement to check that the 
user satisfies the above conditions to be employed (you will need to use an and logical operator).
Please note this version of the program will ask the user to enter all relevant information
first and will then inform the user if they are eligible or not. Note it doesn’t need to 
inform the user of the specific reasons as to why they were not accepted.
"""
def Q2ii():
    
    years_experience = int(input("How many years of software experience do you have?" ))
    micro_cert = input("Do you have a microsoft certificate Y/N?")
    degree = input("Do you have a first class honours undergraduate computing degree Y/N?")
    
    if (years_experience >= 4 and micro_cert == "Y" and degree == "Y"):
        
        print("You are eligible")
        
    else :
        
        print("You do not have the valid requirements")

Q2ii()



"""
A software company sells a package that retails for €99. Quantity discounts are given 
according to the following table. 
Quantity Discount
1 – 9 0%
10 – 19 20%
20 – 49 30%
50 – 99 40%
100 or more 50%
Write a program that will ask the user to enter the number of packages purchased. The 
program should display the amount of the discount (if any) and the total amount of the 
purchase after the discount. Please note that if a user indicates a negative quantity then they 
should be told that the quantity value should be greater than zero.
Please use if elif statements to solve this problem and note that your solution to this problem 
should make use of the and logical operator where possible.
"""

def Q3():
    
    package_cost = float(99)
    quantity_discount = float(1)
    
    num_packages = int(input("How many packages were purchased?"))

    
    
    if(num_packages <= 0) :
        print("The number of packages must be greater than 0")
    

    elif(num_packages >= 10 and num_packages <= 19) :
        quantity_discount = 0.2

    
    elif(num_packages >= 20 and num_packages <= 49) :
        quantity_discount = 0.3
        
    
    elif(num_packages >= 50 and num_packages <= 99) :
        quantity_discount = 0.4

    
    elif(num_packages > 100) :
        quantity_discount = 0.5

    
    total_discount = (package_cost*num_packages)*quantity_discount
    print ("Total Discount is €" , total_discount )
    
    total_cost = (package_cost*num_packages) - total_discount
    print("Total Cost (With Discount) = €" , total_cost )
    
    
    
Q3()
    

"""
(for loops and functions)



(i)

 
You should write a function that will print out the ‘times’ table for a number up to 
a specific limit. The function should take in two parameters. The first value, num, 
is the number that we will multiply by 0, 1, 2, 3, etc. The second number, limit, 
is the number at which we will stop multiplying.

 

So if the user enters 3 as the value of num and 5 as the value of limit then the program
will output the 3 times table from 0 to 5  as shown below.

3*0
3*1
3*2
3*3
3*4
3*5
 
The following is a sample output:


Please enter time tables for printing: 6

Please enter upper limit for multiplication: 4

6*0 = 0

6*1 = 6

6*2 = 12

6*3 = 18

6*4 = 24
"""
def Q4i():
    
    time_table_number = int(input("Please enter time tables for printing: "))
    upper_limit = int(input("Please enter upper limit for multiplication: "))
    
    
    for x in range(upper_limit + 1) :
        ans = time_table_number * x
        print(time_table_number , "*" , x , "=" , ans)


Q4i()


"""
(ii)

 

Implement a function called printNumTriangle. The function should ask the user to 
enter a single integer. It should then print a triangle of that size specified by
the integer so that each row in the triangle is made up of the integer displayed.

 

The following is a sample output

 

Please enter an integer for triangle size: 5

1

22

333

4444

55555
"""

def Q4ii():
    
    triangle_size = int(input("Please enter an integer for triangle size: "))
    
    for x in range(triangle_size + 1) :
        for y in range(x) :
            print((x), end =" ")

        print()
    
Q4ii()


"""
(5)

Write a program that asks the user to enter the rainfall for the first X months
of the year into a list, where X is an int value between 1 and 12. 
(Obtaining the rainfall input from the user should be done using a loop).


The program should calculate and display:

The average monthly rainfall
The highest rainfall value received
The lowest rainfall value received
 

The following is a sample output of this program.

 
How many months of data do you wish to enter: 6

Please enter rainfall for month1 83.6

Please enter rainfall for month2 46.6

Please enter rainfall for month3 97.1

Please enter rainfall for month4 46.4

Please enter rainfall for month5 61.4

Please enter rainfall for month6 164.5

Highest rainfall value: 164.5

Lowest rainfall value: 46.4

Average is 83.2666666667
"""

def Q5():
   
    num_of_months = int(input("How many months of data do you wish to enter: "))
    dataset = []
    total_rainfall = 0
    
    for x in range(num_of_months) :
        print("Please enter rainfall for month" ,(x + 1) , "\t ?")
        rainfall = float(input())
        
        dataset.append(rainfall)
        total_rainfall += rainfall
          
    
    average_rainfall = total_rainfall/num_of_months
    print("Average is " , average_rainfall)
    print("the highest rainfall is \t", max(dataset))
    print("the lowest rainfall is \t", min(dataset))

        
Q5()

"""
(6)

The Fibonacci numbers are the numbers in the following integer sequence:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

 

By definition, the first two numbers in the Fibonacci sequence are 0 and 1,
and each subsequent number is the sum of the previous two.

 

Create a program that creates a list and will populate it with the first 40
Fibonacci numbers (this can be done with just three lines of code).



The program should then ask the user to enter an integer value between
1 and 40 to indicate which number in the Fibonacci series they would
like to see and the application should display that number. 
For example, if the user enters 13, the 13th number is 144.

"""

   
fib = [0, 1]

 

def fib40():

   

    for i in range(2,40):

        fib.append(fib[i-1]+fib[i-2])

    print(fib)

 

def getFib(inx):

    return fib[inx-1]

       

fib40()

print(getFib(13))


"""
Q(7)

Write a program that will act as a basic calculator for the user.
The program should first ask the user for two separate numerical values. 
It should then give the user an option to perform one of four operations:
addition, subtraction, division or multiplication. 
Therefore, if the user selects multiplication then your program should 
print out the product of the two values.  The following is sample output 
from this program.

 

Please enter a numerical value: 12

Please enter a numerical value: 10

Would you like to perform:

1: Addition

2. Subtraction

3. Multiplication

4. Division

> 3

Multiplication of 12 and 10 is 120
"""



"""
My attempt; Works fine but it's less of a calculator and more of a single sum finder.
Adding more fuctions for each operator and a while statement would make it reusable
and faster to run
"""
"""
def Q7():
    
    msg = "Please enter a numerical value:"
    
    num1 = int(input(msg))
    num2 = int(input(msg))
   
    print('''Would you like to perform: 
          \n 1: Addition 
          \n 2. Subtraction 
          \n 3. Multiplication 
          \n 4. Division''')
    
    user_choice = int(input())
    
    #Addition
    if (user_choice == 1) :
        ans = num1 + num2
        
        print("Addition of" , num1 , "and" , num2  , "is" , ans)
    
    #Subtraction
    if (user_choice == 2) :
        ans = num1 - num2
        
        print("Subtraction of" , num1 , "and" , num2  , "is" , ans)
    
    #Multiplication
    if (user_choice == 3) :
        ans = num1 * num2
        
        print("Multiplication of" , num1 , "and" , num2  , "is" , ans)
    
    #Division
    if (user_choice == 4) :
        ans = num1 / num2
        
        print("Division" , "of" , num1 , "and" , num2  , "is" , ans)
    
    
Q7()

"""

def add(num1, num2):

    return num1+num2

 

def subtract(num1, num2):

    return num1-num2

 

def multiply(num1, num2):

    return num1*num2

 

def divide(num1, num2):

    return num1/num2

 

def main():

 

    exitCalc = False   

   

    while exitCalc==False:

       

        num1 = int(input("Please enter number 1: - "))

        num2 = int(input ("Please enter number 2: - "))

       

        option = int(input("Do you want to: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide  :"))

 

        if option == 1:

            result = add(num1, num2)

        elif option ==2:

            result = subtract(num1, num2)

        elif option ==3:

            result = multiply(num1, num2)

        elif option ==4:

            result = divide(num1, num2)

       

        print ("Result is ", result)

       

        exit = input("Do you want to exit y/n")

       

        if exit == 'y':

            exitCalc = True

       

       

main()






