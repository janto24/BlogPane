from django import forms

# App's models
from PaneApp.models import Post, Oportunidades


class NuevoPost(forms.ModelForm):
    #Nuevo Post
    
    class Meta:
        model = Post  # Modelo del cual importa
        fields = [
            'city',
            'resto',
            'subtitle',
            'content',
            'image',
            ]
        #  Widget para agrandar el area de texto(TextField) a 80 columnas
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}


class AgregarDesc(forms.ModelForm):
    #Nuevo Desc

    class Meta:
        model = Oportunidades
        fields = [
            'categoria',
            'descripcion',
            'detalle',
            'valid_through',
        ]
        # Widgets para agrandar el area de texto(CharField) a 80 columnas
        widgets = {
            'descripcion': forms.TextInput(attrs={'size': '80'}),
            'detalle': forms.TextInput(attrs={'size': '80'}),
            'valid_through': forms.SelectDateWidget(),
        }
