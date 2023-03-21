import random
import requests
from PyDictionary import PyDictionary
dictionary = PyDictionary()

def create_dict():

    vowels = ['A', 'E', 'I', 'O', 'U']
    point_dict = {
        1 : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
        2 : ['D', 'G'],
        3 : ['B', 'C', 'M', 'P'],
        4 : ['F', 'H', 'V', 'W', 'Y'],
        5 : ['K'],
        8 : ['J', 'X'],
        10 : ['Q', 'Z'],
    }

    alphabet_dict = {}

    for key in point_dict:
        point_value = key

        for letter in point_dict[key]:
            is_vowel = letter in vowels
            i = ord(letter)
            alphabet_dict[i-64] = {'letter': letter, 'is_vowel': is_vowel, 'point_value': point_value}
    
    return alphabet_dict



def random_letters(dic):
    rand_letters = []
    for i in range(0,25):
        rand_letters.append(dic[random.randint(1,25)]['letter'])
    return rand_letters


def point_value_rand_letters(lis, dic):
    point_values = []
    for letter in lis:
        values = [i for i in dic if dic[i]['letter']==letter]
       
        for value in values:
            point_values.append(dic[value]['point_value'])

    return point_values



def check_if_word_in_dictionary(word):
    
    valid_word = bool(dictionary.meaning(word))

    return valid_word





# for key, letter, value in letter_value:

#     print(str(key)+str(letter)+str(value))

# for key in sorted(a):
#     print ("%s: %s" % (key, a[key]))


