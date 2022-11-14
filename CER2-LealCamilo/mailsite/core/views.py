from django.shortcuts import render
from .models import Mail

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def mail(request):
    mail = Mail.objects.all()

    busqueda = request.GET.get("buscar")

    if busqueda:
        mail = Mail.objects.filter(numero_residencia = busqueda).distinct()
    
    return render(request, 'core/mail.html', {'mail': mail})