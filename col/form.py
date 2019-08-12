from django import forms

class logicForm(forms.Form):
    numero = forms.IntegerField(label='Ingrese un numero')