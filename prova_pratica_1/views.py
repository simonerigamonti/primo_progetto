from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request,"prova_pratica_1/index.html")

def view_a(request):
    a=random.randint(1, 10)
    b=random.randint(1, 10)
    somma = a + b

    if a < b:
        colore_a = "red"
        colore_b = "green"
    elif a > b:
        colore_a = "green"
        colore_b = "red"
    else:
        colore_a = "black"
        colore_b = "black"

    dic = { 'a' : a,
            'b' : b,
            'somma': somma,
            'colore_a': colore_a,
            'colore_b': colore_b,
            }
    return render(request,"prova_pratica_1/view_a.html", dic)

def view_b(request):
    
    return render(request,"prova_pratica_1/view_b.html")

def view_c(request):
    return render(request,"prova_pratica_1/view_c.html")