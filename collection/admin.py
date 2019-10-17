from django.contrib import admin

# import your model
from collection.models import Word

# setup automated slug creation
class WordAdmin(admin.ModelAdmin):
    model = Word
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug' :('name',)}

# Register your models here.
admin.site.register(Word, WordAdmin)
