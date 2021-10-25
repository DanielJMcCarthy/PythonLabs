
"""
Write 4 functions in one python file as follows:
    
a) Takes 5 numbers and return their average.
b) Takes 5 numbers and return the maximum
c) Takes 5 numbers and return the minimum
d) Takes 5 numbers and return those 5 numbers in sorted order (Max to Min)
e) Takes 5 numbers and returns the sum of those numbers
    
    
The file needs to be saved and used as a module in another python file, so that all the functions 
can be called by some given numbers.
"""

#a)
def mean(a , b , c , d , e) :
   
    return (a + b + c + d + e) / 5


#b)
def maximum(a , b , c , d , e) :
    
    return max(max(a,b), max(max(c, d), e) )

#c)
def minimum(a , b , c , d , e) :
    
    return min(min(a,b), min(min(c, d), e) )

#d)
def max_to_min(a , b , c , d , e) :
    
    nums = [a,b,c,d,e]


    nums.sort()

    nums.reverse()


    return nums

#e)
def sum_of(a , b , c , d , e) :
    
    return (a + b + c + d + e)