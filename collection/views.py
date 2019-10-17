from django.shortcuts import render

# Create your views here.
def index(request):
    # defining the variable
    number = 6
    # defining string variable
    thing = "Lucy Lou"
    # passing the variable to the views
    return render(request, 'index.html', {
        'number': number,
        'thing' : thing,
    })
