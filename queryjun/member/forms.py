from django import forms
from django.forms import ModelForm

from django.contrib.auth import authenticate

from .models import Member

class SignUpForm(ModelForm):
    class Meta:
        model = Member
        fields = ('username', 'password', 'password_confirm', 'nickname', 'self_introduce')
        
    username = forms.CharField(label='username', max_length=30, required=True)
    password = forms.CharField(label='password', max_length=30, required=True)
    password_confirm = forms.CharField(label='password_confirm', max_length=30, required=True)
    nickname = forms.CharField(label='nickname', max_length=30, required=True)
    self_introduce = forms.CharField(label='self_introduce', required=True)
        
    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')

        if username and len(username) < 10:
            # raise forms.ValidationError({ 'username': 'Username is too short. Username must be longer than 10 characters.' })
            self.add_error('username', 'Username is too short. Username must be longer than 10 characters.')

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'Password and password confirmation is not same.')

        nickname = cleaned_data.get('nickname')
        self_introduce = cleaned_data.get('self_introduce')

    def save(self, *args, **kwargs):
        member = super().save(commit=False)

        member.username = self.cleaned_data.get('username')
        member.set_password(self.cleaned_data.get('password'))
        member.nickname = self.cleaned_data.get('nickname')
        member.self_introduce = self.cleaned_data.get('self_introduce')

        member.save()

class SignInForm(forms.Form):
    class Meta:
        model = Member
        fields = ('username', 'password')

    username = forms.CharField(max_length=30, label='Username')
    password = forms.CharField(max_length=30, label='Password')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        member = authenticate(username=username, password=password)

        if username and password and not member:
            self.add_error(None, 'Given authentication is not valid information.')