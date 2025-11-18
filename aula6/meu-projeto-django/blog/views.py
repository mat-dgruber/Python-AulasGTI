from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hello_word(request):
     data = [
          {"mensagem":"Olá, Mundo! (API)",
          "status":200}
     ]
     return JsonResponse(data)