
"""
Read and Writing a List To/From 
Files
• Some tasks may require you to save the contents of a list 
to a file so the data can be used at a later time (Use the 
write method in Python file object). 
• Likewise, it may be necessary to read the data from a file 
into a list (Use the readLines methods in Python file 
object).
"""


"""
Writing a List to a File

cities.txt
New York
Boston
Atlanta
Dallas
"""

def main():
    
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']
    
    # Open a file for writing.
    outfile = open('cities.txt', 'w')
    
    # Write the list to the file.
    for item in cities:
        outfile.write(item + '\n') #Use of write method to write a list item to a file
    
    # Close the file.
    outfile.close()
    
main()


"""
Reading a List from a File
"""

def main():
    
    infile = open('cities.txt', 'r')
    
    cities = []
    
    city = infile.readline().rstrip('\n')
    
    while (city != ''):
        cities.append(city)
        city = infile.readline().rstrip('\n')
    
    infile.close()
        
        
    print (cities)
    print (len(cities)) 
    
main()
