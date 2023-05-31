from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .wordgame import create_dict, random_letters, point_value_rand_letters, check_if_word_in_dictionary
from wordgame.models import NewWord
# import inflect
# Create your views here.
# p = inflect.engine()
valid_words = []

def wordgame(request):
    valid_words = []
    alphabet_dicttionary = create_dict()
    keysList = sorted(list(alphabet_dicttionary.keys()))
    rand_letters = random_letters(alphabet_dicttionary)
    point_values = point_value_rand_letters(rand_letters, alphabet_dicttionary)
    letter_value = zip(keysList, rand_letters, point_values)
    return render(request, 'wordgame/wordgame.html', {'letter_value': letter_value})

def fetch_word(request):
    print(request.POST.get('word'))
    if request.method == 'POST':
        word = request.POST.get('word')
        word_points = request.POST.get('word_points')
        #Need to fix logic for plural words using inflect
        result = check_if_word_in_dictionary(word) #func to check if the word is in the english dictionary
        data = {
            'word': word,
            'isValid': result,
            'word_points': word_points
        }
        new_word = NewWord(word=word, isValid=result, pointsValue=word_points)
        new_word.save()
        
    return JsonResponse(data)

    

def pull_valid_words():
    c = NewWord.objects.filter(isValid=True)
    print(c)
