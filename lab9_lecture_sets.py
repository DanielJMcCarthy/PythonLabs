
"""
Set: object that stores a collection of data in the same way 
as a mathematical set.
– All items must be unique. No two elements can have the 
same value.
– Set is unordered
– Elements can be of different data types
"""

"""
set function: used to create a set
– For empty set, call set()
– For non-empty set, call set(argument) where argument is an object that 
contains iterable elements (list or string)
• e.g., argument can be a list 
• If argument contains duplicates, only one of the duplicates will appear in the set
"""




"""
Sets (Creation )
"""

def test_1():
    
    set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    set2 = set(['hello', 'there'])
    set3 = set()
    set4 = set('Testing')
    
    print (len(set1))   #Set1 contains 9 individual numeric elements.
    print (len(set2))   #Set 2 contains two String elements.
    print (len(set3))   #Set 3 is the empty set.
    print (len(set4))   #Set 4 contains 7 String elements.

test_1()



"""
Update can also accept another set as an argument
"""

def test_2():
    
    set1 = set([1,2, 3])
    set2 =set([3, 4, 5, 6])
    set1.update(set2)
    print (set1)

test_2()



"""
Sets (remove method)
"""

def test_3():

    set1 = set()
    set1.update([1, 2, 10, 20])
    print (set1)
    
    num = 1
    if num in set1:
        set1.remove(num)
        print (set1)

test_3()






"""
Sets (Intersection and Union)
"""

def test_4():
    
    set1 = set([1, 2, 3, 4])
    set2 = set([4, 5, 6])
    set3 = set([4, 7, 8, 9])
    set4 = set1 | set2 | set3.union
    print (set4)    #Outputs {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    set5 = set1 & set2 & set3.intersection
    print (set5)    #Outputs {4}

test_4()



"""
Finding the Difference of Sets
• Difference of two sets: a set that contains the elements that 
appear in the first set but do not appear in the second set
• To find the difference of two sets:
• Use the difference method
• Format: set1.difference(set2)
• Use the - operator
• Format: set1 - set2
"""

def test_5():
    
    set1 = set([1, 2, 3, 4])
    set2 = set([4, 5, 6])
    
    difference = set1 - set2;
    print (difference)  #Outputs {1,2,3}

test_5()



"""
Programming Task
• Write a program that will initially gather information on employees 
and their salaries. The program should continue asking the user for 
an employee surname and salary until the user wishes to finish. 
This data should be stored in a dictionary. 
• Next the program should print the total salary bill for the company 
(using only the dictionary)
• It should then print out the list of unique salaries of all employees. 
"""

def task_1_main():
    
    
    employeeDetails = {}
    continueEnteringData = 'y'
    
    while continueEnteringData == 'y':
        surname = input('Please input employee surname')
        salary = int(input('Please input salary'))
        employeeDetails[surname] = salary
        continueEnteringData = input('Enter details for another employee?')
    totalSalaryBill = 0
    
    for key in employeeDetails:
        totalSalaryBill += employeeDetails[key]
    print ("Total Salary: ", totalSalaryBill)
    
    
    uniqueNames = set(employeeDetails.values())           
    print(uniqueNames)

                  
task_1_main()




"""
Programming Task
• Write a basic login program for an application. 
• A file called users.txt contains all the usernames and 
password for all users (sample file shown ). 
• Your program should first read in the contents of this 
file into a dictionary. 
• Can use split command to split a string into individual 
words (returns a list)
• It then asks the user for a username and password 
and print out if they are correct or not. 
"""

def task_2_main():
    
    infile = open('users.txt', 'r')
    #create an empty dictionary
    nameDetails = {}
   
    
   #read each line from the file using a for loop
    for userline in infile:
        data = userline.split()
        if (len(data)== 2):
            nameDetails[data[0]] = data[1]
            
            
    print (nameDetails)
"""        
#Veryfying password

    username = input('Please enter username: ')
    password = input('Please enter password: ')
    
    if (username in nameDetails):
        if (nameDetails[username] == password):
            print("Login Successful”)
        else:
            print("Incorrect Password”)
    
    
    else:
        print ("Unknown Username”)
"""           
task_2_main()