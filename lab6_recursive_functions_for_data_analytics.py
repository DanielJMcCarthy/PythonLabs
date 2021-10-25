
"""
1.Write a function that calculates the nth
Fibonacci number without using any type of 
loop.
"""
#something wrong here ...   <--------
def fib(n):

    if n <= 2:

        return 1

    else:

        return fib(n - 1) + fib(n - 2);

 

print(fib(6))
    



"""
2.Write a function that determines if a number is 
a prime number without using any type of 
loop.
"""

def prime_number() :
    
    num = int(input("Enter a number:"))
    
    if (num / num == 1 and num % 2 > 0) or (num <= 2)  :
        print("That is a prime number.")
    
    else :
        print("That is not a prime number.")

prime_number()
