from django.urls import path
from django.http import HttpResponse

def oiDjango(resquest):
    return HttpResponde('Olá PrimeiroAPP')

urlpatterns = [
    path('olaApp/', oiDjango),
]
