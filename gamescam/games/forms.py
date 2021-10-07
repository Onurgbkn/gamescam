from django import forms

class CommentForm(forms.Form):
    username = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    text = forms.CharField(label='Comment', max_length=200, widget=forms.Textarea(attrs={'class': 'comtextarea form-control', 'rows':'3', 'placeholder':'Comment'}))
    