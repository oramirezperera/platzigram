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


def hi(request):
    """hi"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')] # list comprehension para convertir la lista en numeros
    sorted_int = sorted(numbers) 
    data = {
        'status': 'ok',
        'numbers': sorted_int,
        'message': 'integers sorted successfully',
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')