from django.urls import path

from . import views


urlpatterns = [
    path(""),
    path("composer/", views.ComposerView.as_view()),
    path("composer/<slug:slug>/", views.ComposerDetailView.as_view(), name="composer_detail"),
    path("composer/<slug:parent>/<slug:slug>/", views.PieceOfArtDetailView.as_view(), name="pieceOfArt_detail"),
    path("composer/borodin/<slug:parent>/<slug:slug>/", views.PerDetailView.as_view(), name="per_detail"),
    path("review/rev/r/<int:pk>/", views.AddReviw.as_view(), name="add_review"),

]


