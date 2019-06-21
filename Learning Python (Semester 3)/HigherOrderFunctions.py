#LAB 14
#Due Date: 12/07/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement: Worked with friends and went to recitation               
#
########################################

def makingSound(n,sound):
	#Write your code here
    def fn(size):
        lst = []
        for i in range(size):
            if i % n == 0:
                lst.append(sound)
            else:
                lst.append(i)
        return lst

    return fn

def vectorizing(term):
	#Write your code here
    def other(lst):
        result = []
        for item in lst:
            result.append(fn(item))
        return result

    return other

def square(x):
    return x * x
