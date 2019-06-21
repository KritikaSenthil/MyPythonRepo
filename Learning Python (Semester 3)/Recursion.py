#Lab #7
#Due Date: 10/05/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement:Worked with a friend use stackoverflow             
#  
########################################


#### DO NOT modify the triangle(n) function in any way! 
def triangle(n):
    return recursive_triangle(n, n)
###################
def recursive_triangle(k, n):
    '''
        Takes two integers k and n
        >>> recursive_triangle(2,4)
        '  **\\n   *'
        >>> print(recursive_triangle(2,4))
          **
           *
        >>> triangle(4)
        '****\\n ***\\n  **\\n   *'
        >>> print(triangle(4))
        ****
         ***
          **
           *
    '''
    # --- YOUR CODE STARTS HERE
    output = ' '*(n-k) + '*'*(k)
    if k==1:
        return output
    output += '\\n' + recursive_triangle(k-1, n)
    return output
    print (output)
