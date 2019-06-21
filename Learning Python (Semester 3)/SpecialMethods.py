#Lab #6
#Due Date: 09/30/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement: Worked with a friend              
#  
########################################
import math
class Vector(object):
    '''
        Takes a list and creates a Vector object to perform vector operations
        >>> Vector([1,2])+Vector([5])
        'Error - Invalid dimensions'
        >>> Vector([1,2])+Vector([5,2])
        Vector([6, 4])
        >>> Vector([1,2])-Vector([5,2])
        Vector([-4, 0])
        >>> Vector([1,2])*Vector([5,2])
        9
        >>> x=Vector([2,4,6])
        >>> y=Vector([7,8,9])
        >>> x+y
        Vector([9, 12, 15])
        >>> x-y
        Vector([-5, -4, -3])
        >>> x-Vector([1,2])
        'Error - Invalid dimensions'
        >>> x+5
        'Error - Invalid operation'
        >>> x*y
        100
        >>> x*5
        Vector([10, 20, 30])
        >>> 5*x
        Vector([10, 20, 30])
    '''
    def __init__(self, vector):
        self.vector = vector

    #To compare and determine if both Vector objects are equal
    #Include this in your final submission
    def __eq__(self, other):
        return self.vector==other.vector
    
    def __add__(self, other):
        result = []
        added = tuple( a + b for a, b in zip(self, other) )
        return vector(*added)
    
    def __sub__(self, other):
        result = []
        subbed = tuple( a - b for a, b in zip(self, other) )
        return vector(*subbed)

    def __mul__(self, other):
        if len(self.vector) != len(other.vector):
            return "Error - Invalid dimensions"
        elif isinstance(other, int):
            result = []
            for x in range(len(self.vector)):
                result.append(self.vector[x] * other)
                return Vector(result)

        elif isinstance(other, Vector):
            dot_result = 0
            for y in range(len(self.vector)):
                dot_result += self.vector[y] * other.vector[y]
                return dot_result

    def __rmul__(self, other):
        result = []
        if not (isinstance(other, int) or isinstance(other, Vector)):
            return "Error - Invalid operation"
        elif len(self.vector) != len(other.vector):
            return "Error - Invalid dimensions"
        return self * other
    # --- Your code starts here
       
    # --- ends here
