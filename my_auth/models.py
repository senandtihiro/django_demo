from django.db import models
from django.contrib.auth.hashers import make_password


class UserInfo(models.Model):
    SEX_CHOICES = (
        ('1', '男'),
        ('2', '女'),
    )

    username = models.CharField(max_length=200)
    _password = models.CharField(max_length=100)
    sex = models.SmallIntegerField(choices=SEX_CHOICES, default=2)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_pwd):
        self._password = make_password(raw_pwd)
