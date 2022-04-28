from django.shortcuts import render
from familia.models import Familia


# Create your views here.
def familiar(request):
    miembros = Familia.objects.all()
    return render(request,"familia.html",{"miembros":miembros})