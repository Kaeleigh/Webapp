from django.shortcuts import render
from collection.models import Word

# Create your views here.
def index(request):

    words = Word.objects.all()
    # passing the variable to the views
    return render(request, 'index.html', {
        'words' : words,
    })

def word_detail(request, slug):
    #grab the object
    word = Word.objects.get(slug=slug)
    #pass to the template
    return render(request, 'words/word_detail.html', {
        'word': word,
    })
