"""Platzigram views"""

#Django
from django.http import HttpResponse
from django.http import JsonResponse

# utilities
from datetime import datetime
import json

def hello_world(request):
    """returns a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello, World! The datetime of the server is {now}')


def sort_integers(request):
    """returns a json response with sorted integers"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')] # list comprehension para convertir la lista en numeros
    sorted_int = sorted(numbers) 
    data = {
        'status': 'ok',
        'numbers': sorted_int,
        'message': 'integers sorted successfully',
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    """Returns a greeting"""

    if age < 12:
        message = f'sorry {name} you are not allowed to be here'
    else:
        message = f'Hi {name}! Welcome to Platzigram'
    
    return HttpResponse(message)