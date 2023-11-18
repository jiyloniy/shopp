from django.forms import ModelForm, TextInput, Textarea, EmailInput

from blog.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'phone', 'comment']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'comment': Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }
