from django import forms
from todolist.models import Meta, Task

class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        exclude = ['user',]
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da meta',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição da meta',
                'rows': 3,
            }),
            'previsao_conclusao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user', ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da meta',
            }),
            'meta': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição da meta',
                'rows': 3,
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)

        if user is not None:

            self.fields['meta'].queryset = Meta.objects.filter(user=user)
