from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Meta, Task
from .forms import MetaForm, TaskForm

'''
Neste codigo comentado (#) está uma proposta de alteração para a função home.
O criar_meta ja verifica se o usuario está ativo, e se sim, possibilida o uso da ferramenta.
Minha dúvida é: Como altera-lá e atualizar as outras também.
'''



def criar_meta(request):
    if request.user.is_active:
        if request.method == 'POST':
            form = MetaForm(request.POST)
            if form.is_valid():
                meta = form.save(commit=False)
                meta.user = request.user
                meta.save()
                return redirect('home')
        else:
            form = MetaForm()
        return render(request, 'criar_meta.html', {'form': form})
    return HttpResponseForbidden("Usuário inativo não pode criar metas.")


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


# CREATE, READ, DELETE, UPDATE - Task
# Details meta/task;

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    context_object_name = 'task'
    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})



class TaskDetailView(DetailView):
    # Exibe os detalhes de uma tarefa específica.
    # Usa DetailView, que já cuida de toda a lógica de exibição de detalhes.
    # template_name: Especifica o template que será usado para exibir os detalhes da tarefa.
    # context_object_name: O nome do objeto que será passado ao template.
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'


#UPDATE: Atualizar uma tarefa existente:
class TaskUpdateView(UpdateView):
    # Permite atualizar uma tarefa existente.
    # Usa UpdateView, que cuida da lógica de edição e atualização de um objeto.
    # fields: Especifica quais campos da Task serão exibidos no formulário de atualização.
    # get_success_url: Redireciona para a página de detalhes da tarefa após a atualização bem-sucedida.
    model = Task
    fields = ['name', 'meta', 'description', 'is_active']
    template_name = 'task_form.html'
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})


#DELETE: Excluir uma tarefa
class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Sua tarefa foi excluída com sucesso.')
        return super().delete(request, *args, **kwargs)
