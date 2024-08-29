from django.utils.deprecation import MiddlewareMixin
from posts.models import UserLog
from rest_framework.authentication import TokenAuthentication

class CustomMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        authentication = TokenAuthentication()
        try:
            user, token = authentication.authenticate(request)
            print(user)
            print(request.path)
            UserLog.objects.create(user=user, action=request.path)
        except:
            pass 