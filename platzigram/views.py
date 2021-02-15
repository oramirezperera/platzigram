"""Platzigram views"""

#Django
from django.http import HttpResponse
from django.http import JsonResponse

# utilities
from datetime import datetime

def hello_world(request):
    """returns a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hello, World! The datetime of the server is {now}')


def hi(request):
    """hi"""
    numbers = sorted([int(number) for number in request.GET['numbers'].split(',')])

    return JsonResponse(numbers, safe=False)

