from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'primeiroapp/pages/home.html')

def sobre(request):
    return render(request, 'primeiroapp/pages/sobre.html')