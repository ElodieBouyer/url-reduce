from django.db import models
from django_extensions.db.models import TimeStampedModel

class MinUrl(TimeStampedModel):
    url = models.URLField(max_length=2048, null=False, blank=False)
    token = models.CharField(max_length=16, null=False, blank=False)
    