from django import forms
from todolist.models import Meta

class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = '__all__'    
