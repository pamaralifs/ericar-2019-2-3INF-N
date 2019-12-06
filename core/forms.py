from django import forms
from core.models import Aluno


class AlunoFormInscricao(forms.Form):
    # <option value="" selected="selected" hidden="hidden">Choose here</option>
    INSTRUMENTO_CHOICES = [
        ['', 'Selecione o instrumento'],
        ['Clarone Baixo', 'Clarone Baixo'],
        ['Clarinete', 'Clarinete'],
        ['Fagote', 'Fagote'],
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
    nome = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    instrumento = forms.ChoiceField(label='', 
        initial='', choices=INSTRUMENTO_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    mensagem = forms.CharField(label='', widget=forms.Textarea(
        attrs={'rows': '5', 'class': 'form-control', 'placeholder': 'Sua mensagem'}))
