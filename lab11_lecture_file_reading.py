
"""
Writing Data to a File
• File object’s write method used to write data to the file

– Format: file_variable.write(string)
• File should also be closed using file object close method
– Format: file_variable.close()
"""


def test_main_1():
    
    #write
    customerFile = open('customers.txt', 'w')
    customerFile.write("Java \n")
    customerFile.write("Perl \n")
    customerFile.close()
    
    
    #read
    updatedCustomerFile = open('customers.txt', 'r')
    fileContents = updatedCustomerFile.read();
    updatedCustomerFile.close();
    print (fileContents)

test_main_1()



"""
Writing and Reading Numeric Data
• Strings can be written directly to a file with the write method, 
but numbers must be converted to strings before they can be 
written. 
• Python has a built-in function named str that converts a value 
to a string.
"""

def test_main_2( ) :
    # Open a file for writing.
    outfile = open('numbers.txt', 'w')
    # Get three numbers from the user.
    num1 = input("Enter a number:")
    num2 = input("Enter another number :")
    outfile.write(str(num1) + '\n') #Converts numeric data type to string before writing to file
    outfile.write(str(num2) + '\n')
    outfile.close()


test_main_2()


"""
Writing and Reading Numeric Data
• When we read a value from a file it is read as a String. 
• Therefore, we need a means of converting that value 
from a String to the relevant numerical type. 
• int()
• float()
"""
"""
Program writes a float and integer value to 
file. When we read the numeric values in 
the file we have to convert them from a 
string to an int or float
"""

def test_main_3( ) :
    # Open a file for writing.
    outfile = open('numbers.txt', 'w')
    outfile.write(str(12.3) + '\n')
    outfile.write(str(10) + '\n')
    outfile.close()
    
    updatedFile = open('numbers.txt', 'r')
    number1 = float(updatedFile.readline()); #Convert from Strings to int and float
    number2 = int(updatedFile.readline());
    updatedFile.close()

test_main_3()


"""
• Use a for loop for writing to a file
• Use for and while loop for reading from a file
"""

def test_main_4() :
    
    salesFile = open('sales.txt', 'w')
    numDays = 5
    
    for count in range( 1, numDays + 1 ) :
        # Get the sales for a day.
        sales = input( 'Enter the sales for day ' + str(count) + ': ')
        salesFile.write(str(sales) + '\n')
        
    salesFile.close()
    
test_main_4()



"""
Read Values from a File using Loops
• Often the number of items stored in file is 
unknown
• The readline method uses an empty string as a sentinel when end 
of file is reached
• Can write a while loop with the condition 
while line != ‘’
"""


"""
This programs read from a file 
that contains a single column of 
sales figures (float values)
"""

def test_main_5( ) :
    
    salesFile = open('sales.txt', 'r') 
    line = salesFile.readline() 
    
    while line != '': #When line is equal to the empty string ‘’ we have reached the end of the file and the loop exits
        amount = float(line)  #convert line to a float
        print (amount)
        line = salesFile.readline()
        
    salesFile.close()
    
test_main_5()




"""
for Loop to Read Lines

– Format: 
    for line in file_object:
        statements
        
– The loop iterates once over each line in the file
"""

def test_main_6( ) :
    
    salesFile = open('sales.txt', 'r')
    
    for line in salesFile:
        amount = float(line)
    
    print (amount)
    salesFile.close()
    
test_main_6()

"""
Programming Task
• Write a program that will ask the user to enter employee 
details. The program will first ask the user for the number 
of employees they wish to record. It should then obtain 
the name, ID and department of each employee. The 
program should store this information in a file.

• Write a second program that will open and read the file 
and write the employee information to the screen.
"""

def task_1_write() :
    
    employeeFile = open('employees.txt', 'w')
    
    num = int(input("Enter the number of employees you wish to record: "))
    
    
    for count in range(1 , num + 1) :
        print("Emplyee no.",str(count))
        
        name = input("Enter name: ")
        emp_id = int(input("Enter ID number: "))
        dept = input("Enter department: ")
        
       
        # Write the data as a record to the file.
        employeeFile.write(name + '\n')
        employeeFile.write(str(emp_id) + '\n')
        employeeFile.write(dept + '\n')
    
    employeeFile.close()
    
    
    
task_1_write()


    while line != '': #When line is equal to the empty string ‘’ we have reached the end of the file and the loop exits
        amount = float(line)  #convert line to a float
        print (amount)
        line = salesFile.readline()


def task_1_read() :
    
    employeeFile = open('employees.txt', 'r')
    name = employeeFile.readline()
    
    
    while name != '' :
        

        emp_id = employeeFile.readline()
        dept = employeeFile.readline()
        
        name = name.rstrip('\n')
        dept = dept.rstrip('\n')
        emp_id = emp_id.rstrip('\n')
        
        
        print (' Name : ' , name)
        print (' ID : ' , emp_id)
        print (' Dept : ' , dept)
        
        
        # Read the name field of the next record.
        name = employeeFile.readline()
        
        
        
    employeeFile.close()
    
    
    
task_1_read()



"""
Reading a Line Containing Multiple 
Entries
• Assume we have a file called numbers.txt that contains a 
single line the sequence of numbers
• 55 75 87 
• We want to write a program that will read this line of 
code and add up all three numbers
"""

def test_main_6() :
    
    numbers = numberFile.readline().rstrip('\n')
    numberList = numbers.split()
    
    total = int(numberList[0])+int(numberList[1])+int(numberList[2])
    print (total)
    
    numberFile.close()


test_main_6()



