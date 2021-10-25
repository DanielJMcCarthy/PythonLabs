
import math



"""

Write a function called powerV1. When you call this function (from your main function) it 
should ask the user for a base number and a power number. It should then print out the result 
of raising the base number to the power of the second number. 
Sample output below:

Please enter base number: 3
Please enter power number: 2
The value 3 raised to the power of 2 is : 9
"""
    
def power_v1(base , power):
    
    
    print ("The value of ",base, " raised to the power of ", power, " is: ",base**power)



"""
(ii)
Given the following equation: A = B^C
Write a function called powerV2. When you call this function (from your main function) it 
should ask the user for the power number (C) and the result (A). It should then print out the 
base number. (Hint you need to use math module).
Sample output below:

Please enter power number: 2
Please enter result number: 8
The logarithm of 8 with base 3 is: 3
"""

def power_v2(B , A):
    
    print ("The logarithm of" , A , " base on," , B, ", is: ", math.log(A, B))



"""
Question 3.
Write a program that calculates the factorial of a given value n without using any loop. Hint: 
You should use recursive functions.

                       I Don't understand this one..
"""
def factorial(n):
    
    if n < 1:  

        return 1

    else:

       returnNumber = n * factorial(n - 1) 

      
    return returnNumber

    

print(factorial(5))

factorial()
    


"""
Question 5.

Write a program that takes two number as x and y coordinates of a point in a Cartesian system 
and then calculate the Euclidean distance between the origin of the Cartesian system and the 
point specified by x and y.
Note: Use math module.

Enter X: 5
Enter Y: 3
Euclidean distant: 9.43

                    Another one I don't understand...
"""
def Q5() :
    import math

 

    X = int(input("Enter value for X coordinate: "))

    Y = int(input("Enter value for Y coordinate: "))



    Ecl = math.hypot(X, Y)
 

    print(Ecl)
Q5()



def main():
    
    #i
    base = int(input("Enter the base number: "))
    power = int(input("Enter the power number: "))
    
    power_v1(base , power)
    
    
    #ii
    A = int(input("Enter the value of A: "))
    result = int(input("Enter the result: "))
    
    power_v2(A , result )
    
main()





