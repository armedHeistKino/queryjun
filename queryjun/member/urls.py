from django.urls import path

from .views.member_detail_view import MemberDetailView
from .views.sign_up_view import SignUpView
from .views.sign_in_view import SignInView, sign_out
from .views.guess_history_view import GuessHistoryView

app_name = 'member'

urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign-in'), 
    path('sign-out/', sign_out, name='sign-out'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('<int:member_id>/', MemberDetailView.as_view(), name='member-detail'), 
    path('', MemberDetailView.as_view(), name='member-detail'),
    path('history/<int:member_id>/', GuessHistoryView.as_view(), name='guess-history'), 
    path('history/', GuessHistoryView.as_view(), name='guess-history'), 
]