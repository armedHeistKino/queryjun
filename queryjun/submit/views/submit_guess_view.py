from django import views
from django.http import HttpRequest
from django.utils import timezone
from django.shortcuts import resolve_url, render, redirect

from ..forms import GuessSubmitForm
from ..models import Guess, VendorOption
from ...question.models import Question

class SubmitGuessView(views.View):
    """
        A CBV for processing guess submission & displaying submit guess page
    """
    def get(self, request: HttpRequest, *args, **kwargs):
        """
            Return submit guess page

            :param request:
            :param *args:
            :param **kwargs:
        """
        context = { 
            'question': Question.objects.get(id=kwargs['question_id']), 
            'vendor_option': VendorOption.objects.all(),
        }

        return render(request, '../templates/submit_guess.html', context)
    
    def post(self, request: HttpRequest, *args, **kwargs):
        """
            Redirect when guess is submitted to marking process

            :param request:
            :param *args:
            :param **kwargs:
        """
        form = GuessSubmitForm(request.POST)

        question = Question.objects.get(id=kwargs['question_id'])

        if not form.is_valid():
            context = {
                'form': form,
                'question': question,
                'vendor_option': VendorOption.objects.all()
            }
            return render(request, '../templates/submit_guess.html', context)

        guess = Guess(
            query_guessed=form.cleaned_data.get('query_guess'),
            submit_datetime=timezone.now(),
            selected_vendor=VendorOption.objects.get(id=form.cleaned_data.get('selected_vendor')),
            submitter=request.user,
            question=question
        )
        guess.save()

        return redirect(resolve_url('mark:mark-guess', guess_id=guess.id))