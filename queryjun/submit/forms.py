from django import forms

class GuessSubmitForm(forms.Form):
    query_guess = forms.CharField(max_length=2000, required=True)