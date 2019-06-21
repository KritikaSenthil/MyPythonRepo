#Lab #10
#Due Date: 10/26/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement:             
#  
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        'Queue is empty'
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> print(x)
        Head:Node(2)
        Tail:Node(3)
        Queue:2 3
    '''
    def __init__(self): 
        self.head=None
        self.tail=None

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return ('Head:{}\nTail:{}\nQueue:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def enqueue(self, value):
        x = Node(value)
        x.next = self.head
        self.head = x

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        value = self.tail.value
        self.tail = self.tail.next
        return value
        
        
