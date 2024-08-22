from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Meta, Task
from .forms import MetaForm, TaskForm


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

# CREATE, READ, DELETE, UPDATE - Task
# Details meta/task;

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})

#READ: Detalhes de uma tarefa específica:
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
    fields = ['name', 'meta', 'description', 'is_active', 'user']
    template_name = 'task_form.html'
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={'pk': self.object.pk})

#DELETE: Excluir uma tarefa
class TaskDeleteView(DeleteView):
    # Permite excluir uma tarefa.
    # Usa DeleteView, que já cuida de toda a lógica de exclusão.
    # success_url: Redireciona para uma lista de tarefas após a exclusão bem-sucedida.
    model = Task
    template_name = 'Task_confirm_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
