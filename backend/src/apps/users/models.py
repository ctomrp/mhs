from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
        self,
        first_name: str,
        last_name: str,
        dni: str,
        email: str,
        password: str = None,
        is_staff: bool = False,
        is_superuser: bool = False,
    ) -> "User":
        if not email:
            raise ValueError(_("User must have an email"))
        if not first_name:
            raise ValueError(_("User must have a first name"))
        if not last_name:
            raise ValueError(_("User must have a last name"))
        if not dni:
            raise ValueError(_("User must have a DNI"))

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.dni = dni
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(
        self, first_name: str, last_name: str, dni: str, email: str, password: str
    ) -> "User":
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name=_("First name"))
    last_name = models.CharField(max_length=30, verbose_name=_("Last name"))
    dni = models.CharField(max_length=10, verbose_name=_("DNI"))
    email = models.EmailField(max_length=100, verbose_name=_("Email"), unique=True)
    password = models.CharField(max_length=16, verbose_name=_("Password"))
    username = None
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "dni"]
