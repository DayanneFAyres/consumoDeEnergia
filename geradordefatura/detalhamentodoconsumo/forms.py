from django import forms

class leituraMedidor(forms.Form):
    leitura_atual = forms.CharField(label='Leitura atual', max_length=30)
    leitura_anterior = forms.CharField(label='Leitura anterior', max_length=30)