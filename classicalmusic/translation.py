from modeltranslation.translator import register, TranslationOptions
from .models import Composer, Perfomance, Performers, PieceOfArt, Era, Genre


@register(Composer)
class ComposerTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'placeOfBirth', 'placeOfDeath', 'country')


@register(Performers)
class PerformersTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(PieceOfArt)
class PieceOfArtTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Era)
class EraTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
