from django.db import models
from datetime import date
# Create your models here.
from django.urls import reverse


class Era(models.Model):
    """Эпохи"""
    name = models.CharField("Эпоха", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Эпоха"
        verbose_name_plural = "Эпохи"


class Performers(models.Model):
    """Исполнители"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="pieceOfArt/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Composer(models.Model):
    """Композиторы"""
    name = models.CharField("Имя", max_length=100)
    dateOfBirth = models.DateField("Дата_рождения", default=date.today())
    dateOfDeath = models.DateField("Дата_смерти", default='')
    placeOfBirth = models.CharField("Место_рождения", max_length=100)
    placeOfDeath = models.CharField("Место_смерти", max_length=100)
    country = models.CharField("Страна", max_length=100)
    photo = models.ImageField("Фотография", upload_to="composers/")
    description = models.TextField("Описание")
    eras = models.ForeignKey(
        Era, verbose_name="Эпоха", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("composer_detail", kwargs={"slug": self.url})


    class Meta:
        verbose_name = "Композитор"
        verbose_name_plural = "Композиторы"


class PieceOfArt(models.Model):
    """Произведения"""
    name = models.CharField("Имя", max_length=100)
    composer = models.ForeignKey(
        Composer, verbose_name="композитор", on_delete=models.CASCADE
    )
    dateOfWrite = models.CharField("Дата_написания", max_length=100)
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    description = models.TextField("Описание")
    photo = models.ImageField("Фотография", upload_to="pieceOfArt/", default="top.jpg")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pieceOfArt_detail", kwargs={"slug": self.url, "parent": self.composer.url})

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"


class Perfomance(models.Model):
    """Исполнения"""
    id = models.IntegerField("Номер", unique=True, primary_key=True)
    pieceOfArt = models.ForeignKey(
        PieceOfArt, verbose_name="произведение", on_delete=models.CASCADE
    )
    country = models.CharField("Страна", max_length=100)
    dateOfPlay = models.CharField("Дата_исполнения", max_length=100)
    performers = models.ManyToManyField(Performers, verbose_name="исполнители")
    video = models.FileField("Видео", upload_to="perfomance/")
    url = models.SlugField(max_length=300, unique=True)

    def __str__(self):
        return f"{self.id}: {self.country}, {self.dateOfPlay}"

    def get_absolute_url(self):
        return reverse("per_detail", kwargs={"slug": self.url, "parent": self.pieceOfArt.url})

    class Meta:
        verbose_name = "Исполнение"
        verbose_name_plural = "Исполнения"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="родитель", on_delete=models.SET_NULL, blank=True, null=True)
    perfomance = models.ForeignKey(Perfomance, verbose_name="исполнение", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.perfomance}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
