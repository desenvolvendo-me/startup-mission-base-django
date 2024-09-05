from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from user.permissions import UserIsOwnerMixin
from .models import Meta, Task
from .forms import MetaForm, TaskForm

'''
Neste codigo comentado (#) está uma proposta de alteração para a função home.
O criar_meta ja verifica se o usuario está ativo, e se sim, possibilida o uso da ferramenta.
Minha dúvida é: Como altera-lá e atualizar as outras também.
'''



class CriarMetaView(LoginRequiredMixin, UserIsOwnerMixin, CreateView):
    model = Meta
    form_class = MetaForm
    template_name = 'criar_meta.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if self.request.user.is_active:
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            return HttpResponseForbidden("Usuário inativo não pode criar metas.")

    def get(self, request, *args, **kwargs):
        if not request.user.is_active:
            return HttpResponseForbidden("Usuário inativo não pode criar metas.")
        return super().get(request, *args, **kwargs)



class HomeView(LoginRequiredMixin, UserIsOwnerMixin, ListView, CreateView):
    model = Meta
    template_name = "index.html"
    context_object_name = "metas"
    form_class = MetaForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        return context

    def form_valid(self, form):
        return super().form_valid(form)



class EditarMetaView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Meta
    form_class = MetaForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return Meta.objects.get(id=self.kwargs['id'])




class DeletarMetaView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Meta
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return Meta.objects.get(id=self.kwargs['id'])



# CREATE, READ, DELETE, UPDATE - Task
# Details meta/task;

class TaskCreateView(LoginRequiredMixin, UserIsOwnerMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    context_object_name = 'task'
    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})



class TaskDetailView(LoginRequiredMixin, UserIsOwnerMixin, DetailView):
    # Exibe os detalhes de uma tarefa específica.
    # Usa DetailView, que já cuida de toda a lógica de exibição de detalhes.
    # template_name: Especifica o template que será usado para exibir os detalhes da tarefa.
    # context_object_name: O nome do objeto que será passado ao template.
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'


#UPDATE: Atualizar uma tarefa existente:
class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
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
class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Sua tarefa foi excluída com sucesso.')
        return super().delete(request, *args, **kwargs)
