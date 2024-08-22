from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Meta
from .forms import MetaForm


@login_required
def criar_meta(request):
    if not request.user.is_active:
        return HttpResponseForbidden("Usuário inativo não pode criar metas.")
    '''
    Neste codigo comentado (#) está uma proposta de alteração para a função home.
    O criar_meta ja verifica se o usuario está ativo, e se sim, possibilida o uso da ferramenta.
    Minha dúvida é: Como altera-lá e atualizar as outras também.
    '''
    # if request.method == 'POST':
    #     form = MetaForm(request.POST)
    #     if form.is_valid():
    #         meta = form.save(commit=False)
    #         meta.usuario = request.user
    #         meta.save()
    #         return redirect('lista_metas')
    # else:
    #     form = MetaForm()
    # return render(request, 'metas/criar_meta.html', {'form': form})

def home(request):
    metas = Meta.objects.all()
    if request.method == 'POST':
        form = MetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MetaForm()    
    return render(request, "index.html", {"metas": metas, "form": form})


def editar(request, id):
    meta = Meta.objects.get(id=id)
    return render(request, "update.html", {"meta": meta})


def update(request, id):
    nome = request.POST.get("nome")
    meta = Meta.objects.get(id=id)
    meta.nome = nome
    meta.save()
    return redirect(home)


def delete(request, id):
    meta = Meta.objects.get(id=id)
    meta.delete()
    return redirect(home)

# READ, DELETE, UPDATE - Task
# Details meta/task;
