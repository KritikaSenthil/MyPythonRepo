#Lab #8
#Due Date: 10/12/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement:Consulted stackoverflow and worked with a friend            
#  
########################################


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                                                 
class OrderedLinkedList:
    '''
        Creates a linked list in ascending order
        >>> x=OrderedLinkedList()
        >>> x.pop()
        'List is empty'
        >>> x.add(8)
        >>> x.add(7)
        >>> x.add(3)
        >>> x.add(-6)
        >>> print(x)
        Head:Node(-6)
        Tail:Node(8)
        List:-6 3 7 8
        >>> len(x)
        4
        >>> x.pop()
        8
        >>> print(x)
        Head:Node(-6)
        Tail:Node(7)
        List:-6 3 7
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
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__

    def add(self, value):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > value:
                stop = True
            else:
                previous = current
                current = current.getNext()
            temp = Node(value)
            if previous == None:
                temp.setNext(self.head)
                self.head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)
    
    def pop(self):
        if(self.head==None):
            return None
        if(self.head==self.tail):
            value=self.head.getValue()
            self.head=None
            self.tail=None
            return value
        
        runner =self.head
        while runner.getNext() is not self.tail:
            runner=runner.getNext()
            
            value=self.tail.getValue()
            self.tail=runner 
            self.tail.setNext(None)

            return value

    @property
    def isEmpty(self):
        return self.head == None
        
    def __len__(self):
        return self.count
