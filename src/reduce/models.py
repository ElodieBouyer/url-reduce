from django.db import models
from django_extensions.db.models import TimeStampedModel

import reduce.identifier
import logging

class MinUrl(TimeStampedModel):
    url = models.URLField(unique=True, max_length=2048, null=False, blank=False)
    token = models.CharField(unique=True, max_length=16, null=False, blank=False)

    @classmethod
    def create(cls, url):
        min_url, created = MinUrl.objects.get_or_create(url=url)
        if created:
            min_url.token = reduce.identifier.get_new_identifier()
            min_url.save()
        else:
            logging.info("Duplicated item.")
        return min_url
    