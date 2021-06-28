from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='name')
    comment = forms.CharField(label='comment')