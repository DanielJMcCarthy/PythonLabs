"""
Dictionary: object that stores a collection of data
• Each element consists of a key and a value pair
• To retrieve a specific value, use the key associated with it
• Format for creating a dictionary
• dictionary = {key1:val1, key2:val2}
• To create an empty dictionary:
• dictionary ={}
"""



"""
• Test whether a key is in a dictionary using the in and not in 
operators

"""
def test_1():
    
    details = {'Jim': 'Engineer', 'John': 'Doctor', 'Kevin': 'Chemist'};
    if 'John' in details:
        print (details['John'])

test_1()



"""
To add a new key-value pair:
dictionary[key] = value
• If key exists in the dictionary, the value associated with it will be changed
• If key doesn’t exist in the dictionary, then a new key, value pair is added to the 
dictionary
"""

def test_2():
    
    details = {'Jim': 'Engineer', 'John': 'Doctor', 'Kevin': 'Chemist'};
   
    details['John'] = 'Teacher';
            
test_2()



"""
Task
• Create a program that will ask the user to enter the average grades 
attained by each student and store this data in a dictionary. 
• The program should first ask for the number of students.
• For each student it should ask for the student number and average 
numerical grade. 
• When finished entering data the user should be able to query the 
dictionary by entering a student ID. 
• If the student exists is the dictionary their average grade should be printed
• If not then an error message should be printed. 
"""

def task_1_main():
    
    num_users = int(input("Please enter the number of students: "))
    student_details = {}
    
    for num in range(1, num_users+1):
        student_id = input("Enter student ID ")
        average_grade = float(input("Enter the average grade: "))
        
        student_details[student_id] = average_grade
        


    continue_search = 'y'
    
    while continue_search == 'y':
    
        student_id = input("Please enter student ID: ")
        
        if student_id in student_details :
            print("Average grade of", student_id, "is", student_details[student_id], "%")
        
        else :
            print("Student not found.")
            
        continue_search = input("Do you want to cntinue search y/n: ")
task_1_main()



"""
Delete element from a dictionary
"""

def test_3():
    
    details = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
    
    if 'Name' in details:
        del details['Name']; # remove entry with key 'Name'

test_3()


"""
Dictionaries (Using a list as the value 
element in a Dictionary and the len method)
"""

def test_4():
    
    testScore = {'Scully':[56, 67, 34,],
    'Fitzgibbon':[78, 76, 54]}
    
    print (testScore['Scully']) #prints [56, 67, 34]
    print (len(testScore))  #prints 2


test_4()


"""
Use a for loop to iterate over a dictionary
General format: for key in dictionary:
"""

def test_5():
    ages = {}
    
    #Add a couple of names to the dictionary
    ages['Sue'] = 23
    ages['Peter'] = 19
    ages['Andrew'] = 78
    ages['Karren'] = 45
    
    for key in ages:
        print (ages[key])

test_5()


"""
Using Dictionaries with Methods

Any change made to a dictionary parameter in a function is reflected in 
the original argument.
"""

def test_6_main():
    ages = {}
    ages['Sue'] = 23
    addEntry(ages)
    print (ages)

def addEntry(ages):
    ages['John'] = 13

test_6_main()


