from django import forms

class AddUrlForm(forms.Form):
    url = forms.URLField(label='URL', max_length=2048)