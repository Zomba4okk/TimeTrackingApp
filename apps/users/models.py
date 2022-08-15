from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    user_in_migrations = True

    def _create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError("Email field is missed")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, email: str, password: str = None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff must be True for a admin.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser must be True for a admin.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email",
        null=False,
        blank=False,
        unique=True,
        help_text="User's email (used as login)",
    )
    is_active = models.BooleanField(
        # This field should be used for email confirmation feature.
        # Before the feature will be implemented it will be `True` for all users to not
        #  interfere normal operation of the application
        verbose_name="Is active",
        null=False,
        blank=False,
        help_text="Is user account activated",
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name="Is staff", null=False, blank=False, help_text="Is user admin", default=False
    )
    first_name = models.CharField(
        verbose_name="First name",
        max_length=100,
        null=False,
        blank=False,
        help_text="User's first name",
    )
    last_name = models.CharField(
        verbose_name="Last name",
        max_length=100,
        null=False,
        blank=False,
        help_text="User's last name",
    )

    # The relationship store info about which users are assigned to which projects
    projects = models.ManyToManyField("projects.Project", related_name="users")

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


@receiver(post_save, sender=User)
def generate_token_for_a_new_user(sender, instance: User, created: bool, **kwargs):
    if created:
        Token.objects.create(user=instance)
