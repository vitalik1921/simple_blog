from django.db import models
from django.contrib.flatpages.models import FlatPage


class Page(FlatPage):
    add_name = models.CharField(max_length=200, blank=True)
