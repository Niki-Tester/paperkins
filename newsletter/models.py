import uuid
from django.db import models


class Newsletter(models.Model):
    name = models.CharField(
        max_length=256,
        null=False,
        blank=False,)

    email = models.EmailField(
        max_length=256,
        null=False,
        blank=False,
        unique=True,)

    uid = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        editable=False)

    def __str__(self):
        return self.email

    def _generate_uuid(self):
        """ Generate a random & unique number using UUID """
        return uuid.uuid4().hex

    def save(self, *args, **kwargs):
        """ Override default save method to set uid number """
        if not self.uid:
            self.uid = self._generate_uuid()
        super().save(*args, **kwargs)
