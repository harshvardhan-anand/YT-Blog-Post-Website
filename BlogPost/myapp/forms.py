from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(max_length=50)
    to = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea, required=False)