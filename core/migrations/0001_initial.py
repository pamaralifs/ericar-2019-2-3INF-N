# Generated by Django 3.0 on 2019-12-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('instrumento', models.CharField(choices=[['Clarone Baixo', 'Clarone Baixo'], ['Clarinete', 'Clarinete'], ['Fagote', 'Fagote'], ['Flauta', 'Flauta'], ['Oboé Moderno', 'Oboé Moderno'], ['Piano', 'Piano'], ['Sax Alto', 'Sax Alto'], ['Sax Barítono', 'Sax Barítono'], ['Sax Reto', 'Sax Reto'], ['Sax Tenor', 'Sax Tenor'], ['Trombone de Pisto', 'Trombone de Pisto'], ['Trombone de Vara', 'Trombone de Vara'], ['Trompa Metal', 'Trompa Metal'], ['Trompete', 'Trompete'], ['Tuba', 'Tuba'], ['Violino', 'Violino']], max_length=50, verbose_name='Instrumento Musical')),
                ('mensagem', models.TextField(max_length=500, verbose_name='Mensagem')),
            ],
        ),
    ]
