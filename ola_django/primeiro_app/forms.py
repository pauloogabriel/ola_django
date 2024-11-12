from django import forms
from .models import Pessoa, CategoriaDespesas, SelecionarCategoriaPre

class PessoaCreateForm(forms.ModelForm):
    categorias=forms.ModelChoiceField(
        queryset=CategoriaDespesas.objects.all(),
        initial=CategoriaDespesas.objects.first(),
        label='Categoria Despesas'
    )
    
    interacao=forms.CharField(widget=forms.Textarea)
    class Meta:
        model= Pessoa
        fields='__all__'

class PessoaUpdateForm(forms.ModelForm):
    interacao=forms.CharField(widget=forms.Textarea)
    class Meta:
        model=Pessoa
        fields='__all__'

class CategoriaUpdateForm(forms.ModelForm):
    class Meta:
        model=CategoriaDespesas
        fields='__all__'

class FormDeletePessoa(forms.ModelForm):
    class Meta:
        model=Pessoa
        fields=[]                

class CategoriaDespesasForm(forms.ModelForm):
    class Meta:
        model=CategoriaDespesas
        fields='__all__'

class CategoriaUpdateForm(forms.ModelForm):
    class Meta:
        model=CategoriaDespesas
        fields='__all__'


class FormDeleteCategorias(forms.ModelForm):
    class Meta:
        model=CategoriaDespesas
        fields=[]
        
class FormSelecionarCategorias(forms.ModelForm):
    categorias=forms.ModelChoiceField(
        queryset=CategoriaDespesas.objects.all(),
        initial=CategoriaDespesas.objects.first(),
        label='Categoria Despesas'
        
    )
    
    class Meta:
        model=CategoriaDespesas
        fields=[]   
        