
"""
Question 1.

(a)
Consider the above snippet and modify the code so it can generate 
appropriate error message if a potential error happened. Use 
Exception and Else statements.
"""


def Q1a():
    
    try:

        num1 = int(input('Enter the first number '))

        num2 = int(input('Enter the second number '))

    except ValueError:

        print('The value(s) did not have a right format')

    else:

        average = (num1+num2)/2

        print(average)
Q1a()



"""
(b)

Apply exception and else to catch any potential error. 
Use while loop so the code will iterate until correct value is entered by end-user.
 
"""

def Q1b():
    
    correctValue = True

    while(correctValue):
       
        try:
    
            num1 = int(input('Enter the first number '))
    
            num2 = int(input('Enter the second number '))
    
        except ValueError:
    
            print('The value(s) did not have a right format')
    
        else:
    
            average = (num1+num2)/2
            correctValue = False
            print(average)
Q1b()




"""
Question 2.

Apply appropriate exception statements to catch any potential 
error. Note that the code might need more than one exception
statement.
"""

def Q2():

    try:

        fileContent = open("tes.txt", "r")

        line = fileContent.readline()

        print(line)

        number = int(line)

        print(number)

        fileContent.close()

    except IOError:

        print ("Error: can\'t find file or read data")

    except ValueError:

        print ("The value can not be converted to int")

    else:

        print ("Everything was done")
        
Q2()       
        
        
        
     
"""
Question 3.

Use assert statement to display an appropriate error message for 
any potential error in the code.
"""

def Q3():

    num1 = int(input('Enter a number '))
    
    num2 = int(input('Enter another number '))
    
    assert num2 != 0, "num2 must be non zero for the devision"
    
    print(num1/num2)

Q3()





