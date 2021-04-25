from django.http import HttpResponse


def hello(request):
    return HttpResponse('Olá, Mundo!')


def articles(request, year):
    return HttpResponse(f'O ano enviado foi: {year}')
