from django import forms
from .models import Lounge

class LoungeForm(forms.ModelForm):
    class Meta:
        model = Lounge
        fields = ['title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }
