"""
Question 10.

Use an appropriate data structure and ask end-user to repeatedly enter some names. 
You need to ensure that the items in that data structure can not be altered or 
updated later on.
"""
 

mylist = []


for i in range(3):

    term = input('input a word')

    mylist.append(term)

   
myTuple = tuple(mylist) 

print(type(myTuple))



"""
Question 2.

Create a function that returns a 2-dimentional list of numbers using nested for loops. 
The size of the list must be 10 X 10 and each member/cell of the 2D list will get a 
random number in the range of 1-100. Call your function from the main function and 
print only the 7th row of the list.
"""
 

import random


def myfun():

    lis = []

    for i in range(10):

        nList = []

        for j in range(10):

            nList.append(random.randint(1, 100))

        lis.append(nList)

    return lis

   

def main():

    lis = myfun()

    print(lis[6])

 

main()