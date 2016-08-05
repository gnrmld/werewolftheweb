from django.forms import ModelForm, Select

from .models import Game   

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'max_players')
        

        def __init__(self, *args, **kwargs):
            choices = (i for i in range(6,17))
            self.fields['max_players'] = forms.ChoiceField(choices=choices)