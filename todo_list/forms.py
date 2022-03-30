from django import forms
from .models import TODOList
class TodoForm(forms.ModelForm):
    class Meta:
        model = TODOList
        fields = ['item', 'complete']