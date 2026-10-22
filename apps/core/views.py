from django.shortcuts import render
from categories.models import Category

def home(request):
    # Busca todos os registros gravados no banco da Oracle
    categorias = Category.objects.all()
    return render(request, 'core/home.html', {'categorias': categorias})