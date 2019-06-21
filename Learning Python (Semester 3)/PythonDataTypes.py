#Lab #3
#Due Date: 09/07/2018, 11:59PM
########################################
#
# Name: Kritika Senthil
# Collaboration Statement:
#I referred to this website: https://teamtreehouse.com/community/counting-words-in-a-string-using-a-dictionary-python-collection-challenge
########################################

def countWords(document):
    """
        Takes a string as an argument and returns a dictionary with the word count

        >>> article1='''
        ... He will be the president of the company; right now
        ... he is a vice president.
        ... But he ..... himself,  is no sure of it...
        ... (Later he will see the importance of these.)
        ... '''
        >>> article2='''
        ... Two new vents from the erupting Kilauea volcano on Hawaii
        ... prompted officials on Tuesday afternoon to order the immediate evacuation of
        ... residents remaining in Lanipuna Gardens. All 1,700 residents of Leilani Estates,
        ... as well as the smaller Lanipuna, had previously been ordered to evacuate.
        ... But that does not mean they all have.
        ... '''
        >>> countWords(article1)
        {'he': 4, 'will': 2, 'be': 1, 'the': 3, 'president': 2, 'of': 3, 'company': 1, 'right': 1, 'now': 1, 'is': 2, 'a': 1, 'vice': 1, 'but': 1, 'himself': 1, 'no': 1, 'sure': 1, 'it': 1, 'later': 1, 'see': 1, 'importance': 1, 'these': 1}
        >>> countWords(article2)
        {'two': 1, 'new': 1, 'vents': 1, 'from': 1, 'the': 3, 'erupting': 1, 'kilauea': 1, 'volcano': 1, 'on': 2, 'hawaii': 1, 'prompted': 1, 'officials': 1, 'tuesday': 1, 'afternoon': 1, 'to': 2, 'order': 1, 'immediate': 1, 'evacuation': 1, 'of': 2, 'residents': 2, 'remaining': 1, 'in': 1, 'lanipuna': 2, 'gardens': 1, 'all': 2, 'leilani': 1, 'estates': 1, 'as': 2, 'well': 1, 'smaller': 1, 'had': 1, 'previously': 1, 'been': 1, 'ordered': 1, 'evacuate': 1, 'but': 1, 'that': 1, 'does': 1, 'not': 1, 'mean': 1, 'they': 1, 'have': 1}
        >>> countWords(55)
        'Invalid input'
        >>> countWords([3.5,6])
        'Invalid input'

    """
    # --- YOU CODE STARTS HERE
    if type(document) == str:
        dict = {}
        for word in document.split():
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        print (dict)
    else:
        return "Invalid Input"
    # ---  CODE ENDS HERE

def studentGrades(gradeList):
    """
        Takes a nested list as an argument and returns a list with the average score for each list in integer format

        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],
        ...     ['John', 100, 90, 80],
        ...     ['McVay', 88, 99, 111],
        ...     ['Rita', 45, 56, 67],
        ...     ['Ketan', 59, 61, 67],
        ...     ['Saranya', 73, 79, 83],
        ...     ['Min', 89, 97, 101]]
        >>> studentGrades(grades)
        [90, 99, 56, 62, 78, 95]
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3','Final' ],
        ...     ['John', 100, 90, 80, 90],
        ...     ['McVay', 88, 99, 11, 15],
        ...     ['Rita', 45, 56, 67, 89],
        ...     ['Ketan', 59, 61, 67, 32],
        ...     ['Saranya', 73, 79, 83, 45],
        ...     ['Min', 89, 97, 101, 100]]
        >>> studentGrades(grades)
        [90, 53, 64, 54, 70, 96]
        >>> grades = [
        ...     ['Student', 'Quiz 1', 'Quiz 2'],
        ...     ['John', 100, 90],
        ...     ['McVay', 88, 99],
        ...     ['Min', 89, 97]]
        >>> studentGrades(grades)
        [95, 93, 93]
    """
    # --- YOU CODE STARTS HERE
    l = len(gradeList[0]) - 1
    return [sum(k[1:]) / l for k in gradeList[1:]]


grades = [['Student', 'Quiz 1', 'Quiz 2', 'Quiz 3'],
 ['John', 100, 90, 80],
 ['McVay', 88, 99, 11],
 ['Rita', 45, 56, 67],
 ['Ketan', 59, 61, 67],
 ['Saranya', 73, 79, 83],
 ['Min', 89, 97, 101]]

avgscore = studentGrades(grades)
print(avgscore)
return grades
    # ---  CODE ENDS HERE