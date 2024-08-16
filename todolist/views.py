from django.shortcuts import render, redirect
from .models import Meta
from .forms import MetaForm


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
    vnome = request.POST.get("nome")
    meta = Meta.objects.get(id=id)
    meta.nome = vnome
    meta.save()
    return redirect(home)


def delete(request, id):
    meta = Meta.objects.get(id=id)
    meta.delete()
    return redirect(home)
