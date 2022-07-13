from django import forms

class NameForm(forms.Form):
    user = forms.CharField(label='Your name', max_length=40)
    email = forms.EmailField()
    descripcion = forms.CharField(widget=forms.Textarea)
