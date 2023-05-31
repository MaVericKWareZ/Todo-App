from typing import List

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from model_utils import FieldTracker

from todo_app.general.constants import ACCOUNT_NUMBER_LENGTH
from todo_app.general.validators import HexStringValidator

from ..managers.account import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    account_number = models.CharField(
        max_length=ACCOUNT_NUMBER_LENGTH, primary_key=True, validators=(HexStringValidator(ACCOUNT_NUMBER_LENGTH),)
    )
    display_image = models.URLField(max_length=200, blank=True)
    display_name = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()
    tracker = FieldTracker()

    EMAIL_FIELD = None
    REQUIRED_FIELDS: List[str] = []
    USERNAME_FIELD = 'account_number'

    def __str__(self):
        return f'{self.account_number} | {self.display_name}'

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    @property
    def id(self):  # noqa: A003
        return self.account_number

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
