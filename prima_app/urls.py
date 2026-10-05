from django.urls import path
from prima_app.views import index, home, welcome, menu, chisiamo, variabili

app_name="prima_app"
urlpatterns=[
    path('home', home, name='home'),
    path('welcome',welcome, name='welcome'),
    path('menu', menu, name='menu'),
    path('chisiamo', chisiamo, name='chisiamo'),
    path('variabili', variabili, name='variabili'),
    path('', index, name='index'),
]