from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import datetime, timedelta, timezone
import jwt

from .serializers import UserSerializer
from .models import User
from .authentication import CustomUserAuthentication


class RegisterApi(APIView):
    def post(self, request):
        if request.COOKIES.get("mhs-session"):
            raise AuthenticationFailed(_("You're in a session already"))

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginApi(APIView):
    def post(self, request):
        if request.COOKIES.get("mhs-session"):
            raise AuthenticationFailed(_("You're in a session already"))

        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(raw_password=password):
            raise AuthenticationFailed(_("Invalid credentials"))

        payload = dict(
            id=user.id,
            exp=datetime.now(timezone.utc) + timedelta(hours=16),
            iat=datetime.now(timezone.utc),
        )

        token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
        response = Response()
        response.set_cookie(key="mhs-session", value=token, httponly=True)
        # response.data = {"mhs-session": token}
        return response


class UserApi(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutApi(APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        response = Response(data={_("So long farewell")})
        response.delete_cookie("mhs-session")
        return response
