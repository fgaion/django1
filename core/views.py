from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from core.models import Produto, Cliente

def index(request):
    # print(request) ou print(dir(request)) ou print(request.headers)
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Projeto simples com duas classes: Produto e Cliente',
        'produtos': produtos,
        'clientes': clientes
    }
    return render(request, 'index.html',context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def cliente(request, pk):
    # prod = Produto.objects.get(id=pk)
    cli = get_object_or_404(Cliente, id=pk)

    context = {
        'cliente': cli
    }
    return render(request, 'cliente.html', context)


#As funções abaixo somente funcionam no modo de produção (DEBUG=False)
def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

