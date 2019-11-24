from django.forms import ModelForm
from collection.models import Word

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ('name', 'description',)
