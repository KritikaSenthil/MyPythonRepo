#Lab #5
#Due Date: 09/21/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement: Worked with a friend for the last part and went to office hours on Thursday            
#
########################################


class SodaMachine:
    '''
        Creates instances of the class SodaMachine. Takes a string and an integer

        >>> m = SodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.restock(2)
        'Current soda stock: 2'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(10)
        'Balance: $10'
        >>> m.purchase()
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''
    def __init__(self, product, price):
    #-- start code here ---    
        self.product = product
        self.price = price
        self.stock = 0
        self.balance = 0
    #-- ends here ---

    def purchase(self):
    #-- start code here ---
        if self.stock == 0:
            return 'Product out of stock'
            if self.stock > 0:
                return ('Please deposit $' + str(self.balance))
        else:
            if self.balance >= self.price:
                z = self.balance - self.price
                self.balance = self.balance - self.price
                if z > 0:
                    return (str(self.product) + ' dispensed, take your ' + str(z))
            else:
                z = self.price - self.balance
                return ('Please deposit ' + str(z))
    #-- ends here ---
        
    def deposit(self, amount):
    #-- start code here ---
        if self.stock == 0:
            return ('Sorry, out of stock. Take your $' + str(amount))
        else:
            self.balance = self.balance + amount
            return ('Balance: $' + str(self.balance))
    #-- ends here ---

    def restock(self, amount):
    #-- start code here ---
        self.stock = self.stock + amount
        return ('Current soda stock: ' + str(self.stock))
    #-- ends here ---    

class Line:
    ''' 
       Creates objects of the class Line, takes 2 tuples
        >>> line1=Line((-7,-9),(1,5.6))
        >>> line1.distance
        16.648
        >>> line1.slope
        1.825
        >>> line2=Line((2,6),(2,3))
        >>> line2.distance
        3.0
        >>> line2.slope
        'Infinity'
    '''


    def __init__(self, coord1, coord2):
    #-- start code here ---
        self.coord1 = coord1
        self.coord2 = coord2
    #-- ends here ---
    
    #PROPERTY METHODS
        def distance(self):
    #-- start code here ---
            d = math.sqrt((self.coord1[0] - self.coord2[0])**2 + (self.coord1[1] - self.coord2[1])**2)
            return round(d,3)
    #-- ends here ---
    def slope(self):
    #-- start code here ---
        q = float(self.coord1[0])
        r = float(self.coord1[1])
        s = float(self.coord2[0])
        t = float(self.coord2[1])

        if s == q:
            return "Infinity"

        else:
            m = (t-r) / (s-q)
            return round(m,3)
    #-- ends here ---
       
