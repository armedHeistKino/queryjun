from django import views
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout

from ..forms import SignInForm
from ..models import Member

def sign_out(request: HttpRequest):
    """
        A function for processing sign out
    """
    logout(request)
    return redirect('main:main')

class SignInView(views.View):
    """
        A CBV for processing & displaying sign in page
    """
    def get(self, requets: HttpRequest, *args, **kwargs):
        """
            Returns sign in page

            :param request:
            :param *args:
            :param **kwargs:
        """
        return render(requets, '../templates/sign_in.html')
    
    def post(self, request: HttpRequest, *args, **kwargs):
        """
            Process sign in

            :param request:
            :param *args:
            :param **kwargs:
        """
        form = SignInForm(request.POST)

        if form.is_valid():
            member = self._get_member_authentication(form)

            if not member:
                form = SignInForm()
                return render(request, '../templates/sign_in.html', { 'form': form })
            
            login(request, member)
            return redirect('main:main')

        return render(request, '../templates/sign_in.html', { 'form': form }) 
    
    def _get_member_authentication(self, form: SignInForm) -> Member:
        """
            Authenticate member with provided identification info
            
            :param form: A sign in form
        """
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        auth = authenticate(username=username, password=password)
        return auth