from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploads', verbose_name=_('user'))
    image = models.ImageField(verbose_name=_('image'))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
