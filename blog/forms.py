from django import forms

from blog.models import Comment, Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '名前'}),
            'text': forms.Textarea(attrs={'placeholder': 'コメントを入力してください．'})
        }
        labels = {
            'name': '※必須',
            'text': '※必須'
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '名前'}),
            'text': forms.Textarea(attrs={'placeholder': '返信を入力してください．'})
        }
        labels = {
            'name': '※必須',
            'text': '※必須'
        }