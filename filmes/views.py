from django.shortcuts import render, redirect
from filmes.forms import FilmeForm
from sistema.models import Filme


def cadastrarFilme(request):

    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = FilmeForm()

    return render(
        request, 
        'filmes/cadastrar.html', 
        {'form': form},
        )


def listarFilmes(request):
    filmes = Filme.objects.all()
    
    context = {
        'filmes': filmes,
    }
    
    return render(
        request,
        'filmes/listar.html',
        context,
    )