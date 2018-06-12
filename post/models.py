from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from markdown_deux import markdown

# from comments.models import Comment
# from django.utils import get_read_time


# Create your models here.
# MVC MODEL VIEW CONTROLLER


# Post.objects.all()
# Post.objects.create(user=user, title="Some time")
