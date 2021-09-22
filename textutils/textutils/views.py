from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyse(request):
    return render(request,'analyze.html')

def result(request):
     
    djtxt=request.POST.get('text','default')
    removepunc=request.POST.get('removpunc','off')
    fullcaps=request.POST.get('caps','off')
    removespace=request.POST.get('removspace','off')
    removeline=request.POST.get('removline','off')
    counts=request.POST.get('count','off')
    counter=''
    purposes=''
    if removepunc =="on":

        analyze=''
        punctuations='''!()-[];:'"/,<>.\|@#$%&*_-+{}='''
        for char in djtxt:
            if char not in punctuations:
                analyze= analyze + char 

        djtxt=analyze
        purpose='remove punctuations'
        purposes+=purpose
        params={'purpose':purposes,'analyzed_text':analyze}
        return render(request,'result.html',params)
    if(fullcaps =="on"):
        analyze=''
        for char in djtxt:
            analyze= analyze + char.upper()
        djtxt=analyze
        purpose='upper case'
        purposes+=purpose
        params={'purpose':purposes,'analyzed_text':analyze}
        return render(request,'result.html',params)
    elif(removeline=='on'):
        analyze=''
        for char in djtxt:
            if char !="\n" and char !="\r":
                analyze=analyze+char
        djtxt=analyze
        purpose='remove line'
        purposes+=purpose
        params={'purpose':purposes,'analyzed_text':analyze}
        return render(request,'result.html',params)
    elif(counts =="on"):
        counter= len(djtxt)
        purpose='remove punctuations'
        purposes+=purpose
        params={'purpose':purposes,'analyzed_text':analyze }
        return render(request,'result.html',params)
    elif(removespace=='on'):
        analyze=''
        for index,char in enumerate(djtxt):
            if not(djtxt[index]==' 'and djtxt[index+1]==' '):
                analyze=analyze+char
        djtxt=analyze
        purpose='remove space'
        purposes+=purpose
        params={'purpose':purposes,'analyzed_text':analyze}
        return render(request,'result.html',params)
    else:
        return HttpResponse("error")
