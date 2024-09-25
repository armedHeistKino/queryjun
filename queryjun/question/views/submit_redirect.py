from django.http import HttpRequest
from django.shortcuts import resolve_url, redirect

def submit_redirect(request: HttpRequest, question_id):
    """
        A FBV redirects when requests submit page
        - Submitting guess requires sign in

        :param request:
        :param question_id:
    """
    if request.user.is_authenticated:
        return redirect(resolve_url('submit:submit-guess', question_id=question_id))
    else:
        return redirect('member:sign-in')