
"""
(1) Using conditional statements and logical operators write a python 
code that satisfies the following condition:
    
If salary more than 40 and you are older than 25 or if you have worked 
25 years and have kid you can apply for mortgage.


salary40 = False
age25 = False
work25 = True
kid = True
"""


salary40 = False
age25 = False
work25 = True
kid = True

def state1_1(salary40, age25, work25, kid):

    if salary40 and age25 or work25 and kid:

        print("yes")

    else:

        print("no")
        
state1_1(salary40, age25, work25, kid)
 
    
    
def state1_2(salary40, age25, work25, kid):

    if (salary40 and age25) or (work25 and kid):

        print("yes")

    else:

        print("no")
        
state1_2(salary40, age25, work25, kid)



"""
(2) Using conditional statements and logical operators write a python 
code that satisfies the following condition:
    
If salary more than 40 or you are older than 35 and if you have worked 
10 years or you have a kid you can apply for mortgage.
"""



salary40 = False
age35 = False
work10 = True
kid = True


def state2_1(salary40, age35, work10, kid):
    
    if (salary40 > 40) or (age35 and work10) or (kid):
        
        print("yes")
        
    else:
        
        print("no")
        
    
state2_1(salary40, age35, work10, kid)