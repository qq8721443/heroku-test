from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bucket(models.Model):
    title = models.CharField(verbose_name= 'TITLE', max_length=50)
    content = models.CharField(verbose_name = 'CONTENT', max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', null=True, blank=True)

    def __str__(self):
        return self.title
