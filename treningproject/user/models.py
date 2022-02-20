from django.contrib.auth import get_user_model
from django.db import models

from .constants import SPECIALIZATION_CHOICES

User = get_user_model()


class Doctor(User):
    specialization = models.IntegerField(choices=SPECIALIZATION_CHOICES)
