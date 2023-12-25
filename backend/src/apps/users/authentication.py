import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _

from .models import User


class CustomUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("mhs-session")

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed(_("Token has expired"))
        except jwt.InvalidTokenError:
            raise AuthenticationFailed(_("Invalid token"))

        user = User.objects.filter(id=payload["id"]).first()
        return (user, None)
