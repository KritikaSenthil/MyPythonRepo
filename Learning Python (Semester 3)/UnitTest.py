#Lab #4
#Due Date: 09/14/2018, 11:59PM
########################################
#                                      
# Name:Kritika Senthil
# Collaboration Statement:             
#Worked with my friend for the unittest part of the lab
########################################

    """
        Takes a string and an integer an returns the encrypted message using the Caesar cipher method 
        >>> encrypt("Hello world",12)
        'Tqxxa iadxp'
        >>> encrypt("We are Penn State!!!",6)
        'Ck gxk Vktt Yzgzk!!!'
        >>> encrypt("We are Penn State!!!",5)
        'Bj fwj Ujss Xyfyj!!!'
        >>> encrypt(5.6,3)
        'Invalid input'
        >>> encrypt('Hello',3.5)
        'Invalid input'
        >>> encrypt(5.6,3.15)
        'Invalid input'
    """
    # --- YOU CODE STARTS HERE
def encrypt(message, key):
    if type(message) == str and type(key) == int:
        cipherMsg = ""
        for ch in message:
            if ch.isalpha():
                a = ord(ch) + key
                if a > ord('z'):
                    a -= 26
                final = chr(a)
            cipherMsg += final
        print("Your message is: ", cipherMsg)
        return cipherMsg
    else:
        print("Invalid Input")

    # ---  CODE ENDS HERE

    """
        Takes a string and an integer an returns the decrypted message using the Caesar cipher method 
        >>> decrypt("Tqxxa iadxp",12)
        'Hello world'
        >>> decrypt("Ck gxk Vktt Yzgzk!!!",6)
        'We are Penn State!!!'
        >>> decrypt("Bj fwj Ujss Xyfyj!!!",5)
        'We are Penn State!!!'
        >>> decrypt(5.6,3)
        'Invalid input'
        >>> decrypt('Hello',3.5)
        'Invalid input'
        >>> decrypt(5.6,3.15)
        'Invalid input'
    """

    # --- YOU CODE STARTS HERE
def decrypt(message, key):    
    if type(message) == str and type(key) == int:
        cipherMsg = ""
        for ch in message:
            if ch.isalpha():
                b = ord(ch) - key
                if b > ord('z'):
                    b -= 26
                final = chr(b)
            cipherMsg += final
        print("Your message is: ", cipherMsg)
        return cipherMsg
    else:
        print("Invalid Input")

    # ---  CODE ENDS HERE




