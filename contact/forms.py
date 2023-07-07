from django import forms
from .models import message

class CommentForm(forms.ModelForm):
    class Meta:
        model = message
        fields = ('name', 'email', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        
