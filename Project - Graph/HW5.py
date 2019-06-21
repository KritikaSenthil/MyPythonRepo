#HW 5
#Due Date: 12/07/2018, 11:59PM
########################################
#
# Name: Kritika Sentihil
# Collaboration Statement: Worked with friends and used udemy online
#
########################################

# ---Copy your code from labs 9 and 10 here (you can remove their comments)  
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None  

    def __str__(self):
        return "Node({})".format(self.value) 
    __repr__ = __str__                        

class Stack: 
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
        if self.top is None:
            return True
        return False

    def __len__(self):
        count = 0
        temp = self.top
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def peek(self):
        return self.top.value
    def push(self,value):
        if self.top is None:
            self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            return ("Stack is empty")
            return None
        else:
            final = self.top.value
            self.top = self.top.next
            return final
        
class Queue:
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
        if (self.head == None):
            return True
        else:
            return False

    def __len__(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.next
        return count

    def enqueue(self, value):
        temp = Node(value)
        if self.head == None:
            self.tail = temp
            self.head = temp
        else:
            temp.prev = self.tail
            temp.prev.next = temp
            self.tail = temp

    def dequeue(self):
        if self.isEmpty() == True:
            return 'Queue is empty'
        elif self.isEmpty()== False:
            x = self.head
            self.head = self.head.next
            return x.value
        
#----- HW5 Graph code     
class Graph:
    def __init__(self, graph_repr=None):
        if graph_repr is None:
            self.vertList = {}
        else:self.vertList = graph_repr

    def addVertex(self,key):
        if key not in self.vertList:
            self.vertList[key] = []
            return self.vertList

    def addEdge(self,frm,to,cost=1):
        if frm not in self.vertList:
            self.addVertex(frm)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[frm].append((to, cost))
        return self.vertList

    def bfs(self, start):
    	# Your code starts here
        main= []
        q = Queue()
        main.append(start)
        q.enqueue(start)
        while q.isEmpty()==False:
            templst= []
            temp = q.dequeue()
            p = self.vertList[temp]
            if len(p) != 0:
                if type(p[0])==tuple:
                    for i in p:
                        templst.append(i[0][0])
                else:
                   for i in p:
                        templst.append(i)
                templst.sort()
                for i in templst:
                    if i not in main:
                        main.append(i)
                        q.enqueue(i)
        return main

    def dfs(self, start):
    	# Your code starts here
        s=Stack()
        main=[]
        x=[]
        s.push(start)
        while s.isEmpty()==False:
            temp=s.pop()
            v=reversed(sorted(self.vertList[temp]))
            if temp not in main:
                main.append(temp)
            for i in v:
                if type(i)==tuple:
                    temp2=i[0]
                else:
                    temp2=i
                if temp2 not in main:
                    s.push(temp2)
        return main

    ### EXTRA CREDIT, uncomment method definition if submitting extra credit
    def dijkstra(self,start):
        # Your code starts here
        short = {}
        prev_node = {}
        novisit = {}
        novisit.update(self.vertList)
        for node in novisit:
            short[node] = 1000000000
        short[start] = 0
        while novisit:
            min_node = None
            for node in novisit:
                if min_node is None:
                    min_node = node
                elif short[node] < short[min_node]:
                    min_node = node
            extra = self.vertList[min_node]
            for childNode, distance in extra:
                if distance + short[min_node] < short[childNode]:
                    short[childNode] = distance + short[min_node]
                    prev_node[childNode] = min_node
            novisit.pop(min_node)
        for i in short.keys():
            if short[i] == 1000000000:
                short[i] = 'Infinite'
        return short
