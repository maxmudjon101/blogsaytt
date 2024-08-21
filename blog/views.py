from django.shortcuts import render

# Create your views here.
def homView(request):
    return render(request,"home.html")
def NewsView(request):
    return render(request,"news.html")

def kataktWiev(request):
    return render(request,"kantakt.html")
def jahonWiev(request):
    return render(request,"jahon.html")

def sportWiev(request):
    return render(request,"sport.html")

