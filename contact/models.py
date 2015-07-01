from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField('Nome', max_length= 100)
    email = models.EmailField('E-mail')
    suject = models.CharField('Assunto', max_length= 100)
    message = models.TextField('Mensagem')