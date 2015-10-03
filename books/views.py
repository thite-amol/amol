from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'search_text' in request.GET:
        message = 'You searched for: {0}' .format(request.GET['search_text'])
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
