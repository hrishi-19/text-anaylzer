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
    params={}
    if removepunc =="on":
        analyze=''
        punctuations='''!()-[];:'"/,<>.\|@#$%&*^_-+{}='''
        for char in djtxt:
            if char not in punctuations:
                analyze= analyze + char 
        counter=len(analyze)
        params={'analyzed_text':analyze,'counts':counter }
        djtxt=analyze
        
    if(fullcaps =="on"):
        analyze=''
        for char in djtxt:
            analyze= analyze + char.upper()
        counter=len(analyze)
        params={'analyzed_text':analyze,'counts':counter }
        djtxt=analyze
       
    if(removeline=='on'):
        analyze=''
        for char in djtxt:
            if char !="\n" and char !="\r":
                analyze=analyze+char
        counter=len(analyze)
        params={'analyzed_text':analyze,'counts':counter }
        djtxt=analyze
       
    if(removespace=='on'):
        analyze=''
        for index,char in enumerate(djtxt):
            if not(djtxt[index]==' 'and djtxt[index+1]==' '):
                analyze=analyze+char
        counter=len(analyze)
        params={'analyzed_text':analyze,'counts':counter }

    if(removepunc!='on' and fullcaps !='on' and removespace !='on'  and removeline !='on'):
        return HttpResponse("Please select the any stwiches")


    return render(request,'result.html',params)
   
