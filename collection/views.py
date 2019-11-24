from django.shortcuts import redirect, render
from collection.forms import WordForm
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

def edit_word(request, slug):
    #grab the object
    word = Word.objects.get(slug=slug)
    #sets the form i am using
    form_class = WordForm
    #condition for coming to this view from submitted form
    if request.method == 'POST':
        #grab data from submitted form
        form = form_class(data=request.POST, instance=word)
        if form.is_valid():
            #save new data
            form.save()
            return redirect('word_detail', slug=word.slug)

    #otherwise create the form
    else:
        form = form_class(instance=word)

    #render the template
    return render(request, 'words/edit_word.html', {
        'word': word,
        'form': form,
    })
