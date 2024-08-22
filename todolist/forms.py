from django import forms
from todolist.models import Meta, Task

class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'meta', 'description', 'is_active', 'user']
