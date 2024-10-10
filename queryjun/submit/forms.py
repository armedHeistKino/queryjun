from django import forms

class GuessSubmitForm(forms.Form):
    selected_vendor = forms.IntegerField(required=True)
    query_guess = forms.CharField(max_length=2000, required=True)