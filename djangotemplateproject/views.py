from django.shortcuts import render

# def index(request):
#    return HttpResponse("Projekt index wurde aufgerufen!")

def index(request):
    # home.html aus dem Template Verzeichnis laden.
    return render(request, 'home.html')


def impressum(request):
    return render(request, 'impressum.html')
