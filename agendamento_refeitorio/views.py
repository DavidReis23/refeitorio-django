from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # ou outro nome do HTML

def agendCard(request):
    return render(request, 'agendCard.html')

def cardapio_semanal(request):
    return render(request, 'cardapio_semanal.html')

def telaCardSemanal(request):
    return render(request, 'telaCardSemanal.html')
