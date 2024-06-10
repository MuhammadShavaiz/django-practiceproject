from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')
def about(request):
    return HttpResponse("This is About page")
def contact_me(request):
    return HttpResponse('contact me: +92 3206877289')
def analyze(request):
    djangotext = request.GET.get('text', 'default')
    action = request.GET.get('action', 'off')
    if not djangotext:
        return HttpResponse('No Text Added')
    else:
        if action == 'removpunc':
            pur = "punctuation removed"
            rem_punct = ""
            punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
            for char in djangotext:
                if char not in punc:
                    rem_punct = rem_punct + char
            params = {'purpose':pur, 'removed_punctuations':rem_punct}
            return render(request, 'analyze.html',params)
        elif action == 'capital':
            cap = 'Capitalized Text'
            capital_text = ""
            for char in djangotext:
                capital_text = capital_text + char.upper()
            params = {'purpose':cap, 'removed_punctuations':capital_text}
            return render(request, 'analyze.html',params)