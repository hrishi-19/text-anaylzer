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
    djtxt=request.POST.get('text','default')
    removepunc=request.POST.get('removpunc','off')
    fullcaps=request.POST.get('caps','off')
    removespace=request.POST.get('removspace','off')
    removeline=request.POST.get('removline','off')
    counts=request.POST.get('count','off')
    #analyse text
    if removepunc =="on":

        analyze=''
        punctuations='''!()-[];:'"/,<>.\|@#$%&*_-+{}='''
        for char in djtxt:
            if char not in punctuations:
                analyze= analyze + char 

        djtxt=analyze
        params={'purpose':'remove punctuations','analyzed_text':analyze}
        return render(request,'analyze.html',params)
    if(fullcaps =="on"):
        analyze=''
        for char in djtxt:
            analyze= analyze + char.upper()
        djtxt=analyze
        params={'purpose':'uppercase','analyzed_text':analyze}
        return render(request,'analyze.html',params)
    elif(removeline=='on'):
        analyze=''
        for char in djtxt:
            if char !="\n" and char !="\r":
                analyze=analyze+char
        djtxt=analyze
        params={'purpose':'remove line','analyzed_text':analyze}
        return render(request,'analyze.html',params)
    elif(counts =="on"):
        analyze= len(djtxt)
        params={'purpose':'uppercase','analyzed_text':analyze}
        return render(request,'analyze.html',params)
    elif(removespace=='on'):
        analyze=''
        for index,char in enumerate(djtxt):
            if not(djtxt[index]==' 'and djtxt[index+1]==' '):
                analyze=analyze+char
        djtxt=analyze
        params={'purpose':'remove line','analyzed_text':analyze}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("error")