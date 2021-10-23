# -*- coding: utf-8 -*-
"""
This is just a fun one to see if I understand operator precendence..



Operator Precedence
not     High
and     Medium
or      Low


Write the equivalent expressions to each of the following logic expressions in python:
    
A or B and C or D
A or B or C and D
A or B or C and D or E
not A and B or not C and D
A and B or not C
"""

# My attempt
A or B and (C or D)
A or B or (C and D)
(A or B or C) and (D or E)
(not ( A and B) or not(C and D))
(A and B) or (not C)

#Solution
:
    
A or D or (B and C)
A or B or (C and D)
A or B or E or (C and D)
((not A) and B) or ((not C) and D)
(A and B) or (not C)

"""
I was way off XD ->
So I guess make sure to assign brackets in terms of Operator Precendence.
"""