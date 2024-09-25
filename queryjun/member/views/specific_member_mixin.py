"""
    FYI

    Use when making a service where it requires member
    - it returns specific member when the member id is given
    - or it returns member who signed in
    - else it raise DoesNotExist Exception

    Example:

    class MemberRequiredView(SpecificMemberMixin, ..., views.View):
        (...)
"""

from django.http import HttpRequest

from ..models import Member

class SpecificMemberMixin(object):
    """
        Mixin class for fetching member        
    """
    def get_specific_member(self, request: HttpRequest, *args, **kwargs) -> Member | Exception:
        """
            fetch member from database with given member_id or from sign in session
            else raise DoesNotExist exception

            :param request: 
            :param *args:
            :param **kwargs:
        """
        if 'member_id' in kwargs:
            return Member.objects.get(id=kwargs['member_id'])

        if request.user.is_authenticated:
            return request.user
        
        raise Member.DoesNotExist