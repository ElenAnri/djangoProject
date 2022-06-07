from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Composer, Era, Genre, Performers, PieceOfArt, Perfomance
from  .forms import ReviewForm

# Create your views here.


class ComposerView(ListView):
    """Список композиоров"""
    model = Composer
    queryset = Composer.objects.filter(draft=False)
    template_name = "classicalmusic/composer_list.html"


class ComposerDetailView(DetailView):
    """Полное описание композитора"""
    model = Composer
    slug_field = "url"


class PieceOfArtDetailView(DetailView):
    """Полное описание композитора"""
    model = PieceOfArt
    slug_field = "url"


class PerDetailView(DetailView):
    """Полное описание композитора"""
    model = Perfomance
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context


class AddReviw(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Perfomance.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            #if request.POST.get("parent", None):
            #    form.parent_id = int(request.POST.get("parent"))
            form.perfomance = movie
            form.save()
        return redirect(movie.get_absolute_url())

def get(request):
    performers = Performers.objects.all()
    return render(request, "classicalmusic/composer_detail.html", {"performers_list": performers})


class PerformersView(View):
    """Список композиоров"""
    model = Performers
    queryset = Performers.objects.all()
    template_name = "classicalmusic/performer_list.html"


@login_required
def set_language(request):
    lang = request.GET.get('l', 'en')
    request.session[settings.LANGUAGE_SESSION_KEY] = lang
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    return response


