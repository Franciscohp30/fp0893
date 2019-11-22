from django.shortcuts import render, redirect
from cadastrar.models import Clientes
from cadastrar.form import FormClientes



def home(request):
	return render(request, 'website/index.html')


def cadastraClientes(request):
    form = FormClientes(request.POST or None, request.FILES or None)
    if form.is_valid():
    	form.save()
    	return redirect('url_listar')
    return render(request,'website/cadastro.html', {'form': form } )

def listaClientes(request):
    clientes= Clientes.objects.all()
    return render(request,'website/lista.html', {'clientes': clientes } )





