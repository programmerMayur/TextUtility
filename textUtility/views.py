# this file created by mayur
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    extraSpace = request.POST.get('extraSpace','off')
    newLine = request.POST.get('newLine','off')
    charCount = request.POST.get('charCount','off')
    fullCap = request.POST.get('fullCap','off')
    # analyedText = djtext
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^`{|}~'''
    analyedText = ""
    # This is remove punctuation from text
    if removepunc == "on":
        for char in djtext:
            if char not in punctuation:
                analyedText = analyedText + char
        params = {'purpose':'Remove Punctuation','inputText':djtext , 'analyzedText':analyedText}

    # This is Remove New Line from text
    elif newLine == "on":
        analyedText2 = ""
        for char in djtext:
            if char != "\n"and char != "\r":
                analyedText = analyedText + char
            else:
                analyedText = analyedText + " "
        for index, char in enumerate(analyedText):
            if not(analyedText[index]==" "  and analyedText[index+1]==" ") :
                analyedText2 = analyedText2 + char
        params = {'purpose': 'Remove New Line', 'inputText': djtext, 'analyzedText': analyedText2}

    # This is Remove Extra Spaces from text
    elif extraSpace == "on":
        for index, char in enumerate(djtext):
            if not(djtext[index]==" "  and djtext[index+1]==" ") :
                analyedText = analyedText + char


        params = {'purpose': 'Remove New Line', 'inputText': djtext, 'analyzedText': analyedText}

    # This is count length of text
    elif charCount == "on":
        lengthText = len(djtext)
        params = {'purpose': 'Find the length of String', 'inputText': djtext, 'analyzedText':  f"Length of String : {lengthText}"}

    # This is convert text to upper case
    elif fullCap == "on":
        for char in djtext:
            analyedText = analyedText + char.upper()
        params = {'purpose': 'Convert to FULL CAP', 'inputText': djtext, 'analyzedText': analyedText}


    else:
        return HttpResponse("<h1>Error</h1><br><h3>Select Option before Submit</h3>")

    return render(request,'analyze.html',params)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
