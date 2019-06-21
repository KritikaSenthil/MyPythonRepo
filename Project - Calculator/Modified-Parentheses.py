#HW 4
#Due Date: 11/16/2018, 11:59PM
########################################
#                                      
# Name: Kritika Senthil
# Collaboration Statement: Worked with a friend and consulted stackoverflow and udemy            
#
########################################

#Name:

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__                    

# ----    Copy your Stack (or Queue) code from LAB9 (or LAB10) here ---------
class Stack:
    '''
        Creates an empty Stack with support for push and pop operations
        >>> x=Stack()
        >>> x.pop()
        'Stack is empty'
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__
    
    def isEmpty(self):
        return self.top is None
            
    def __len__(self):
        count = 0
        temp = self.top
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def peek(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.top.value

    def push(self,value):
        x = Node(value)
        x.next = self.top
        self.top = x

    def pop(self):
         if self.isEmpty():
            return 'Stack is empty'
         value = self.top.value
         self.top = self.top.next
         return value
# ----    Stack (or Queue) code ends here here ---------

def findNextOpr(txt):
    #--- Copy your function code from HW3 here ----#
    """
        Takes a string and returns -1 if there is no operator in txt, otherwise returns 
        the position of the leftmost operator. +, -, *, / are all the 4 operators

        >>> findNextOpr('  3*   4 - 5')
        3
        >>> findNextOpr('8   4 - 5')
        6
        >>> findNextOpr('89 4 5')
        -1
    """
    if len(txt)<=0 or not isinstance(txt,str):
        return "type error: findNextOpr"
    else:
        operators='^*/+-'
        for i in range (0,len(txt)):
            a=txt[i]
            for j in range (0,len(operators)):
                b=operators[j]
                if a==b:
                    return i
        if a!=b:
            return -1
    #--- function code ends -----#

def isNumber(txt):
    #--- Copy your function code from HW3 here ----#
    """
        Takes a string and returns True if txt is convertible to float, False otherwise 

        >>> isNumber('1   2 3')
        False
        >>> isNumber('-  156.3')
        False
        >>> isNumber('29.99999999')
        True
        >>> isNumber('    5.9999 ')
        True
    """
    if len(txt)==0 or not isinstance(txt, str):
        return "type error: isNumber"
    try:
        tmp = float(txt)
        return True
    except ValueError:
        return False
    #--- function code ends -----#

def getNextNumber(expr, pos):
    #--- Copy your function code from HW3 here ----#
    """
        expr is a given arithmetic formula of type string
        pos is the start position in expr
          1st returned value = the next number (None if N/A)
          2nd returned value = the next operator (None if N/A)
          3rd retruned value = the next operator position (None if N/A)

        >>> getNextNumber('8  +    5    -2',0)
        (8.0, '+', 3)
        >>> getNextNumber('8  +    5    -2',4)
        (5.0, '-', 13)
        >>> getNextNumber('4.5 + 3.15         /   5',0)
        (4.5, '+', 4)
        >>> getNextNumber('4.5 + 3.15         /   5',10)
        (None, '/', 19)
    """
    try:
        if len(expr)==0 or not isinstance(expr, str) or not isinstance(pos, int) or pos<0:
            return None, None, "error"
            #--- continue the rest of the code here ---#
        if expr[pos:].strip()[0]=="-":
            x = expr.find("-", pos)+1
            a = findNextOpr(expr[x:])
            if a==-1:
                oprPos=-1
            else:
                oprPos= x+a - pos
        else:
            oprPos=findNextOpr(expr[pos:])
        if oprPos==-1:
            nextOpr=None
            oprPos=None
            nextNumber=expr[pos:]
        else:
            oprPos = pos + oprPos
            nextOpr = expr[oprPos]
            nextNumber = expr[pos:oprPos]
        if isNumber(nextNumber):
            nextNumber=float(nextNumber)
        else:
            nextNumber=None
        return nextNumber, nextOpr, oprPos
    except:
        return None, None, "error"
    #--- function code ends -----#
    
def exeOpr(num1, opr, num2):
    #This funtion is just an utility function. It is skipping type check
    if opr=="+":
        return num1+num2
    elif opr=="-":
        return num1-num2
    elif opr=="*":
        return num1*num2
    elif opr=="/":
        if num2==0:
            print("Zero division error")
            return "error"
        else:
            return num1/num2
    elif opr=="^":
        return num1 ** num2
    else:
        print("error in exeOpr")
        return "error"
    
def _calculator(expr):
    #--- Copy the body of your calculator(expr) function from HW3 here ----#
    """
        Takes a string and returns the calculated result if the arithmethic expression is value,
        and error message otherwise 

        >>> _calculator("   -4 +3 -2")
        -3.0
        >>> _calculator("-4 +3 -2 / 2")
        -2.0
        >>> _calculator("-4 +3   - 8 / 2")
        -5.0
        >>> _calculator("   -4 +    3   - 8 / 2")
        -5.0
        >>> _calculator("23 / 12 - 223 + 5.25 * 4 * 3423")
        71661.91666666667
        >>> _calculator("2 - 3*4")
        -10.0
        >>> _calculator("4++ 3 +2")
        'error'
        >>> _calculator("4 3 +2")
        'input error line B: calculator'
        >>> _calculator("4^2 / 2^2")
        4.0
        >>> _calculator(" 3 + 2^5")
        35.0
        >>> _calculator(" 3^2 + 4^2")
        25.0
        >>> _calculator("  2^2 * 5 + 3^2 / 2^3 ")
        21.125
        >>> _calculator("  2^5 / 2^3 *5 /  2^3 / 5")
        0.5
        >>> _calculator("-5 + 60 / 3^3 * 4 - 2 * 4^2")
        -28.11111111111111
        >>> _calculator("4+2*-4+1")
        -3.0
        >>> _calculator("-4^ / 2^2")
        'error'
        >>> _calculator("- 3.4546 ^ 0.3423 * + 3.234")
        'error'
    """

    if len(expr)<=0 or not isinstance(expr,str):
        return "input error line A: calculator"
    expr = expr.strip()
    if expr[0]!="-":
        newNumber, newOpr, oprPos = getNextNumber(expr, 0)
    else:
        newNumber, newOpr, oprPos = getNextNumber(expr, 1)
        newNumber *= -1
    if newNumber is None:
        return "input error line B: calculator"
    elif newOpr is None:
        return newNumber
    elif newOpr=="+" or newOpr=="-":
        mode="add"
        mulResult=1          
        addResult=newNumber     
        mulLastOpr='*'
    elif newOpr=="*" or newOpr=="/":
        mode="mul"
        addResult=0
        addLastOpr='+'
        mulResult=newNumber
    elif newOpr=='^':
        mode='exp'
        addResult=0
        mulResult=1
        addLastOpr='+'
        mulLastOpr='*'
        expResult=newNumber
    pos=oprPos+1                
    opr=newOpr                  
    while True:
        newNumber, newOpr, oprPos = getNextNumber(expr, pos)
        if newNumber == None:
            return 'error'
        elif newOpr is None and mode == 'add':
            return exeOpr(addResult, opr, newNumber)
        elif newOpr is None and mode == 'mul':
            mulResult = exeOpr(mulResult, opr, newNumber)
            return exeOpr(addResult, addLastOpr, mulResult)
        elif newOpr is None and mode == 'exp':
            expResult = exeOpr(expResult, opr, newNumber)
            mulResult = exeOpr(mulResult, mulLastOpr, expResult) 
            return exeOpr(addResult, addLastOpr, mulResult)
        elif newOpr=='^' and mode == 'exp':
            expResult = exeOpr(expResult,opr,newNumber)
        elif newOpr=='^' and mode == 'mul':
            expResult = newNumber
            mulLastOpr = opr
            mode = 'exp'
        elif newOpr=='^' and mode == 'add':
            expResult = newNumber
            addLastOpr = opr
            mode = 'exp'
        elif (newOpr == '*' or newOpr == '/') and mode == 'exp':
            expResult = exeOpr(expResult,opr,newNumber)
            mulResult = exeOpr(mulResult,mulLastOpr,expResult)
            mode = 'mul'
        elif (newOpr == '*' or newOpr == '/') and mode == 'mul':
            mulResult = exeOpr(mulResult,opr,newNumber)
        elif (newOpr == '*' or newOpr == '/') and mode == 'add':
            mulResult = newNumber
            addLastOpr = opr
            mode = 'mul'   
        elif (newOpr == '+' or newOpr == '-') and mode == 'exp':
            expResult = exeOpr(expResult,opr,newNumber)
            addResult = exeOpr(addResult,addLastOpr,expResult)
            mulResult=1
            mode = 'add'
        elif (newOpr == '+' or newOpr == '-') and mode == 'mul':
            mulResult = exeOpr(mulResult,opr,newNumber)
            addResult = exeOpr(addResult,addLastOpr,mulResult)
            mulResult=1
            mode = 'add'
        elif (newOpr == '+' or newOpr == '-') and mode == 'add':
            addResult = exeOpr(addResult,opr,newNumber)

        pos = oprPos+1             
        opr = newOpr 
    #--- function code ends -----#

def calculator(expr):
    # Required: calculator must create and use a Stack (or Queue) for parenthesis matching
    # Call _calculator to compute the inside parentheses
    if not isinstance(expr,str) or len(expr)<=0: 
        return "input error in calculator"
    expr = expr.strip()
    s = Stack()        # You must use the Stack s
    ##OR
    #q = Queue()

    #Scan the expression to find the most inner expression, note that if pos==-1 you can try to compute the expression as is
    pos = expr.find("(")
    while True:
    #--- function code starts here -----#
        """
>>> calculator("3*(10 - 2*3)") 12.0
>>> calculator(" -2 / (- 4) * (3 - 2*( 4- 2^3)) + 3") 8.5
>>> calculator("2*(4+2*(5-3^2)+1)+4") -2.0
>>> calculator("-(-2)*10 - 3*(2 - 3*2) ") 32.0
>>> calculator("-(-2)*10 - 3*(2 - 3*2)) ") error
>>> calculator("-(-2)*10 - 3*/(2 - 3*2) ") error
"""
        if pos == -1:
            return _calculator(expr)
        final = expr.find(")", pos + 1)
        if final == -1:
            return 'error'
        newPos = expr.find("(", pos + 1)
        if 0<= newPos < final:
            s.push(pos)
            pos = newPos
        else:
            end = _calculator(expr[pos+1 : final])
            if isinstance(end, str):
                return end
            end=int(end)
            expr = expr[:pos] + str(end) + expr[final +1:]
            if not s.isEmpty():
                pos = s.pop()
            else:
                pos = expr.find("(")
    #--- function code ends here-----#
