functions_exercise

def is_two(n):
    return n == 2 or n =='2'

def is_vowel(char):
    if type(char) == str: 
        return char.lower() in list('aeiou')
    else:
        return False