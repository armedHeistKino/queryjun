from django import views
from django.http import HttpRequest
from django.shortcuts import render, redirect

from ..forms import SignUpForm
    
class SignUpView(views.View):
    """
        A CBV for processing sign up & displaying sign in page
    """
    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Return sign up page

            :param request: 
            :param *args:
            :param **kwargs:
        """
        return render(request, '../templates/sign_up.html')
    
    def post(self, request: HttpRequest, *args, **kwargs):
        """
            Process sign up page

            :param request:
            :param *args:
            :param **kwargs:
        """
        form = SignUpForm(request.POST)

        if form.is_valid():     
            form.save()
            return redirect('main:main')
        
        return render(request, '../templates/sign_up.html', { 'form': form })