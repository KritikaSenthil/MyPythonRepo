#LAB 13
#Due Date: 11/18/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement:Went to recitation             
#
########################################

def merge(list1, list2):
	#write your code here
    result = []
    a = b = 0
    total = len(list1) + len(list2)
    while len(result) != total:
        if len(list1) == a:
            result += list2[b:]
            break
        elif len(list2) == b:
            result += list1[a:]
            break
        elif list1[a] < list2[b]:
            result.append(list1[a])
            a += 1
        else:
            result.append(list2[b])
            b += 1
    return result

def mergeSort(numList):
	#write your code here
    if len(numList) == 1:
        return numList
    
    else:
        mid = len(numList)//2
        left = numList[:mid]
        right = numList[mid:]

        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left, right)
        
        

        

    

    

    

        
