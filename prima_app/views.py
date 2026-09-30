from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"prima_app/home.html")

def welcome(request):
    return render(request,"prima_app/welcome.html")

def menu(request):
    return render(request,"prima_app/menu.html")

def chisiamo(request):
    return render(request,"prima_app/chisiamo.html")

def variabili(request):
    context= { 'var1': '10', 'var2': 'ciao', 'var3': '123 hello world'}
    return render(request,"prima_app/variabili.html", context)

def index(request):
    return render(request,"prima_app/index.html")