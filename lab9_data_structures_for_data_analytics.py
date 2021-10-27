
"""

Question 1. 

Write a function that asks end-user to enter name and studentID for each student and 
store them in a dictionary where the studentID is the key and the name is its value. The 
program should generate appropriate message if end-user tried to provide a key that is 
already existing in the dictionary.

"""

def newFunction():

   
    YesNo = 'y'

    students = {}

    while YesNo == 'y':

        name = input('enter the student name  ')

        studentID = int(input('enter the student ID  '))

        if studentID in students:

            print('the detail of this student is available  ')

        else:

            students[studentID] = name

            

        YesNo = input('do you want to continue? y or n?  ')

    return students
    

newFunction()


"""
Question 2.
Using list to set conversion, write a short function to only find the number of items that 
are repeated more than once in the list.
"""


def Q2(my_list):
  
    myset = set(my_list)

    return (len(my_list) - len(myset))
    
Q2()



"""
Question 3.
Write a Python script to merge two Python dictionaries.
"""
def Q3():

    first = {123:'Daniel', 234 : 'McCarthy'}
    
    second  = {345: 'Dara', 456: 'Daly' }
    
     
    first.update(second)
    
    print(first)   

Q3()


"""
Question 4.
Write a Python program to map two lists into a dictionary.
"""

def capitals() :

    first = ['paris', 'madrid', 'dublin']
    
    second = ['france','spain', 'ireland']
    
    myDictionary = dict(zip(first, second))
    
    print(myDictionary)


capitals()

"""
Question 5.
Write a function that creates a dictionary using a for loop. 
Keys being the numbers starting from 1 to 10 inclusive and values
are being some random values in the range [1 - 20] inclusive.
Then separate the keys from values and add them in two lists.
"""

def Q5() :
    
    mm = dict()
    
    
    
    #for i in range(11):
    
       # mm[i+1] = rnd.randint(1, 20)
    

    keys = list(mm.keys())
    
    values = list(mm.values())
    
      
    print(mm)
    
    print(keys)
    
    print(values)


Q5()

"""
Question 6.
Write a Python program to print all unique values in a dictionary.
"""
 
def Q6():
    

    mm = dict()
    
     
    
   # for i in range(11):
    
        #mm[i+1] = rnd.randint(1, 20)
    
    
    
    keys = list(mm.keys())
    
    values = set(mm.values())
    
     
    
    print(mm)
    
    print(keys)
    
    print(values)


Q6()

"""
Question 7.

Write a function that takes two sets as input, 
then it should return only those values that were not common among both sets.

"""

 

def nonCommon(s1, s2):

    return s1^s2

s1 = {1, 2, 3, 4, 5, 6}
    
s2 = {10, 20, 30, 4, 5, 6}
    
print(nonCommon(s1, s2))


"""
Question 8.
Write a program that goes through a list and extract only integer values
and add them in a new list.
"""

def Q8() :

    mylist = [1, 4, 5.5, 'da', 4, "aa"]
        
    
    emp = []
    
    for i in mylist:
    
        if type(i) == int:
    
            emp.append(i)
    
            print(i)
    
           
    
    print(emp)

Q8()

"""
Question 9.

Repeat the previous program this time only extract unique numbers (integer).
""" 
def Q9() :
    
    mylist = [1, 4, 5.5, 'da', 4, "aa"]   
    
    
    emp = set()
    
    for i in mylist:
    
        if type(i) == int:
    
            emp.add(i)
    
            print(i)
    
           
    
    print(emp)
    
Q9()  
    

"""
Question 10.

Use an appropriate data structure and ask end-user to repeatedly enter some names.
You need to ensure that the items in that data structure can not be altered or 
updated later on.
"""
 

def Q10():
    

    mylist = []
    
    for i in range(3):
    
        term = input('input a word')
    
        mylist.append(term)
    
       
    
    myTuple = tuple(mylist)
    
     
    
    print(type(myTuple))
    print(myTuple)
    
Q10()   
    
    
    
    
    
    
    
    
    