from django.urls import path
from seconda_app.views import esempio_if, if_else_elif

app_name="seconda_app"
urlpatterns=[
    path('es_if', esempio_if, name='es_if'),
    path('if_else_elif', if_else_elif, name='if_else_elif'),
]