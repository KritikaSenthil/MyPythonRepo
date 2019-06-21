#LAB 12
#Due Date: 11/18/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement: Worked with my friend and went to recitation          
#
########################################


def bubbleSort(numList):
        '''
                Takes a list and returns 2 values
                1st returned value: a dictionary with the state of the list after each complete pass of bubble sort
                2nd returned value: the sorted list

                >>> bubbleSort([2,3,5,4,1])
                ({1: [2, 3, 4, 1, 5], 2: [2, 3, 1, 4, 5], 3: [2, 1, 3, 4, 5], 4: [1, 2, 3, 4, 5]}, [1, 2, 3, 4, 5])
        '''
        # Your code starts here
        a = {}
        for i in range(1, len(numList)):
                for j in range(len(numList) - 1):
                        if numList[j] > numList[j + 1]:
                                numList[j], numList[j + 1] = numList[j + 1], numList[j]
                a[i] = numList.copy()
        return (a, numList)
                       

 
