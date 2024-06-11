from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')
def about(request):
    return HttpResponse('I am Muhammad Shavaiz Butt and this is my first django project')
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
            params = {'purpose':pur, 'analyzed_text':rem_punct}
            return render(request, 'analyze.html',params)
        elif action == 'capital':
            cap = 'Capitalized Text'
            capital_text = ""
            for char in djangotext:
                capital_text = capital_text + char.upper()
            params = {'purpose':cap, 'analyzed_text':capital_text}
            return render(request, 'analyze.html',params)
        elif action == 'lower':
            low = 'lowered Text'
            lower_text = ""
            for char in djangotext:
                lower_text = lower_text + char.lower()
            params = {'purpose':low, 'analyzed_text':lower_text}
            return render(request, 'analyze.html',params)