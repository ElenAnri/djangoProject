from django import  forms
from django.forms import TextInput, EmailInput, Textarea

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма отзыва"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
        widgets = {
            "name": TextInput(attrs={"class": "form-control border"}),
            "email": EmailInput(attrs={"class": "form-control border"}),
            "text": Textarea(attrs={"class": "form-control border"})
        }

