from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class Contato(models.Model):
    first_name = models.CharField(max_length=50)
    last_name0 = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    descripion = models.TextField(blank=True, verbose_name='Descrição')
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Categoria')

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name0}'


