from django import forms
from .models import Lounge
from .models import Comments, Reply


class LoungeForm(forms.ModelForm):
    class Meta:
        model = Lounge
        fields = ['title', 'content', 'image', 'is_anonymous']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }
    is_anonymous = forms.BooleanField(required=False, label='익명으로 작성')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content', 'image']
       
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content', 'image']