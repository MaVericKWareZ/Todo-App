from django.db import models

from todo_app.accounts.models import Account
from todo_app.general.models import CreatedModified


class Task(CreatedModified):
    creator = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} | {self.creator.display_name}'
