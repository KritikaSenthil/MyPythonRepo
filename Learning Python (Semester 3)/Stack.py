#Lab #9
#Due Date: 10/19/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement:Worked with a friend and consulted stackoverflow             
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

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
