from django import forms
from django.contrib import admin

# Register your models here.
from .models import Composer, Era, Perfomance, Performers, PieceOfArt, Reviews, Genre
from modeltranslation.admin import TranslationAdmin


admin.site.register(Composer)
admin.site.register(Era)
admin.site.register(Perfomance)
admin.site.register(Performers)
admin.site.register(PieceOfArt)
admin.site.register(Reviews)
admin.site.register(Genre)

