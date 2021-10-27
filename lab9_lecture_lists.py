"""
Lists are dynamic data structures, meaning that items may be added to them or 
removed from them. 
• List: an object that contains multiple data items
– Element: An item in a list
– Format: list = [item1, item2, etc]
– Can hold items of different types
"""



"""
Task
• Write a program that will ask the user to enter an
upper limit for a list
• It should then generate a list between 0 and the
upper limit and print out the contents of the list.
• Your program should then print the contents of the
list in reverse order. 

"""
def gen_list() :
    
    limit = int(input("Please enter upper limit of list"))
    numbers = list(range(limit+1))
    print (numbers)
    index = len(numbers)-1
    while index>=0:
        print (numbers[index]),
        index -= 1

gen_list()




"""
Concatenation example -> lists
"""
def concatenate() :
    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = list1+list2
    # list3 now contains [1, 2, 3, 4, 5, 6]
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1 += list2
    #(changes contents of list1 to [1, 2, 3, 4, 5, 6])

    print(list3)
    
concatenate()


"""
Slice: a span of items that are taken from a sequence

– List slicing format: list[start : end]

– Span is a list containing copies of elements from start up to, but not including,
end

• If start not specified, 0 is used for start index
• If end not specified, len(list) is used for end index
"""


def slice() :
    
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday']
    midDays = days[2:5]
    # Would output ['Tuesday', 'Wednesday', 'Thursday']. 
    print(midDays)
    
    
    midDays = days[:2]
    # Would output ['Sunday', 'Monday'].
    print(midDays)    
    

    midDays = days[5:]
    # Would output ['Friday', 'Saturday '].   
    print(midDays)
    
    
    midDays = days[2:7:2]
    # Would output ['Tuesday', 'Thursday', 'Saturday'].
    print(midDays)
    
    
    midDays = days[-2:]
    # Would output ['Friday', 'Saturday '].
    print(midDays)

    
slice()


"""
Task
• Create a list containing the following integer values 2, 4, 6, 8, 10,
12, 14.
• 1. Use list slicing to return a list containing the values between 8-14
inclusive from the list above
• 2. Use list slicing to obtain the values 4, 8, 12 from the list above
"""

def slice_2() :

    simpleList=[2, 4, 6, 8, 10, 12, 14]
    sublist1 = simpleList[3:]
    sublist2 = simpleList[1::2]
    print (sublist1)
    print (sublist2) 
    
slice_2()


"""
Task
• Write a python program that will generate a list between 0 and
1000
• Use list slicing to print out all numbers in the list that are evenly
divisible by 5
"""
    
def slice_3() :
    
    numbers = list(range(1000))
    divisibleNumbers = numbers[5::5]
    print (divisibleNumbers)
        
slice_3()


"""
Finding Items in Lists with the in Operator
"""

"""
def find() :
    
    # code will output “Found list item” as the value 12 appears
    # in the list numbers
    numbers = [12, 43, 56]
    userNumber = 12
    
    if userNumber in numbers :
        print(“Found list item”)

find()
"""

def bulit_in_functions():
    
    #insert
    days = ['Sunday']
    newDay = 'Tuesday'
    days.append(newDay)
    days.insert(1, 'Monday');
    print(days)
    # Will output ['Sunday', 'Monday', 'Tuesday']
    
    #delete
    myList = [1, 2, 3, 4 , 5]
    print ('Before deletion:', myList)
    del myList[ 2 ]
    print ('After deletion:', myList)
    # Would output
    # Before deletion: [1, 2, 3, 4, 5]
    # After deletion: [1, 2, 4, 5]

    #sort , reverse
    myList= [9, 1, 0, 2, 8, 6, 7 , 4, 5]
    print ('Original order:', myList)
    myList.sort()
    print ('Sorted order:', myList)
    myList.reverse();
    print ('Reverse Sorted order:', myList)
    # Original order: [9, 1, 0, 2, 8, 6, 7, 4, 5]
    # Sorted order: [0, 1, 2, 4, 5, 6, 7, 8, 9]
    # Reverse Sorted order: [9, 8, 7, 6, 5, 4, 2, 1, 0]
    
    

"""
Exercise
• We want to record the grades of a student in a list.
• We should first ask the user for the total number of
subjects and then the individual grades for subject 1,
subject 2 etc and store these values in a list
• Next we will loop through the list to obtain the
average grade
"""

def record_grades() :
    
    totalNumberSubjects = int(input("How many subjects do you have"))
    allNumbers = []
    
    for num in range(totalNumberSubjects):
        num = int(input("Please enter grade for subject"))
        allNumbers.append(num)
    
    print (allNumbers)
    total = 0.0
        
    for num in allNumbers:
        total+= num
    
    print ("Average grade is ", total/len(allNumbers))

record_grades()


"""
Split Function
• The split function: returns a list containing the words
in the string
• By default, uses space as separator
• Can specify a different separator by passing it as an
argument to the split method
"""

def split():
    
    data = 'John,Doe,1984,4,1,male'
    tokens = data.split(',')
    firstName = tokens[0]
    lastName = tokens[1]
    print (firstName, lastName)
    
split()


"""
Task
• Ask the user to input a single line sentence from the
command line
• Your program should then print out the number of
words in the sentence with 3 or less characters
"""

def main_1 () :
    text = input('Please input a sentence')
    words = text.split()
    count = 0
    for word in words:
        if len(word)<=3:
            count+=1
        
    print ('Total number of words with or less chars', count) 

main_1()












