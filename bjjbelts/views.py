from django.shortcuts import redirect

def index(request):
    response = redirect('/bjjquestionnaire/')
    return response
