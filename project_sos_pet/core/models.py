from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    petname = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=20, blank=False)   
    zone = models.CharField(max_length=100, blank=False)
    description = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=False)
    tipo = models.CharField(
        max_length=1,
        choices=(
            ('C', 'Cachorro'), 
            ('G', 'Gato')
            ))
    castrado = models.CharField(
        max_length=1,
        default='P',
        choices=(
            ('P', 'Não sei informar'), 
            ('S', 'Sim'), 
            ('N', 'Não')
            ))
    sexo = models.CharField(
        max_length=1,
        choices=(
            ('M', 'Macho'), 
            ('F', 'Fêmea')
            ))
    vacinado = models.CharField(
        max_length=1,
        default='P',
        choices=(
            ('P', 'Não sei informar'), 
            ('S', 'Sim'), 
            ('N', 'Não'), 
            ('I', 'Incompleto')))
    temperamento = models.CharField(
        max_length=1,
        default='D',
        choices=(
            ('D', 'Dócil'), 
            ('A', 'Ativo'), 
            ('B', 'Brabo'), 
            ))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    end_date = models.DateTimeField(null=True, blank=True)
    begin_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='pet')

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'pet_lost'

