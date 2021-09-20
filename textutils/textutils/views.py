from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return render(request,'index.html')
def removeline(request):
    return HttpResponse('''<a href="/">back</a>''')
def capfirst(request):
    return HttpResponse('''<a href="/">back</a>''')
def removepunc(request):
    #get text
    djtxt=request.GET.get('text','default')
    print(djtxt)
    #analyse text
    return HttpResponse('''<a href="/">back</a>''')
def removespace(request):
    return HttpResponse('''<a href="/">back</a>''')
def removline(request):
    return HttpResponse('''<a href="/">back</a>''')
def analyse(request):
     #get text
    djtxt=request.GET.get('text','default')
    removepunc=request.GET.get('removpunc','off')
    print(removepunc)
    print(djtxt)
    #analyse text
    if removepunc =="on":

        analyze=''
        punctuations='''!()-[];:' "/,<>.\|@#$%&*_-+{}='''
        for char in djtxt:
            if char not in punctuations:
                analyze=analyze + char 
        
        params={'purpose':'remove punctuations','analyzed_text':analyze}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("error")