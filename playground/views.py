from django.shortcuts import render
from django.http import HttpResponse
def say_hello(request):
    return render(request, 'hello.html')
def about(request):
    return HttpResponse("This is About page")
def youtube(request):
    return HttpResponse('''<h1>shavaiz</h1><a href = "https://www.youtube.com">visit youtube!</a>''')
def analyze(request):
    djangotext = request.GET.get('text', 'default')
    action = request.GET.get('action', 'off')
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