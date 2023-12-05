from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر آواتار', null=True, blank=True)
    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    mobile = models.CharField(max_length=11, verbose_name='تلفن همراه', unique=True)
    national_code = models.CharField(max_length=10, verbose_name='کد ملی')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()

        return self.email

    def clean(self):
        super().clean()
        if User.objects.filter(mobile=self.mobile).exclude(id=self.id).exists():
            raise ValidationError({'mobile': 'این شماره تلفن قبلا استفاده شده است.'})
