"""Platzigram views"""
from django.http import HttpResponse


def hello_world(request):
    """returns a greeting"""
    return HttpResponse('Hello, World!')

