from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.models import Evento


# Create your views here.
#def index(request):
    #return redirect('/agenda/')
def eventos(request, titulo_evento):
    evento = Evento.objects.get(titulo= titulo_evento)
    return HttpResponse(evento.local)

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request,'core/agenda.html', dados)
