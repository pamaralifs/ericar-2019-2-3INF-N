from django.db import models

# Create your models here.


class Aluno(models.Model):
    INSTRUMENTO_CHOICES = [
        ["Clarone Baixo", "Clarone Baixo"],
        ["Clarinete", "Clarinete"],
        ["Fagote", "Fagote"],
        ['Flauta', 'Flauta'],
        ['Oboé Moderno', 'Oboé Moderno'],
        ['Piano', 'Piano'],
        ['Sax Alto', 'Sax Alto'],
        ['Sax Barítono', 'Sax Barítono'],
        ['Sax Reto', 'Sax Reto'],
        ['Sax Tenor', 'Sax Tenor'],
        ['Trombone de Pisto', 'Trombone de Pisto'],
        ['Trombone de Vara', 'Trombone de Vara'],
        ['Trompa Metal', 'Trompa Metal'],
        ['Trompete', 'Trompete'],
        ['Tuba', 'Tuba'],
        ['Violino', 'Violino'],
    ]
    nome = models.CharField(max_length=40, verbose_name='Nome')
    email = models.EmailField(max_length=255, verbose_name='E-mail')
    instrumento = models.CharField(
        choices=INSTRUMENTO_CHOICES, max_length=50, verbose_name='Instrumento Musical')
    mensagem = models.TextField(max_length=500, verbose_name='Mensagem')

    def __str__(self):
        return self.nome
