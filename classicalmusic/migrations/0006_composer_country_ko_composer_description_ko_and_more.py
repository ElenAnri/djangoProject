# Generated by Django 4.0.4 on 2022-06-08 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classicalmusic', '0005_remove_composer_country_kor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='composer',
            name='country_ko',
            field=models.CharField(max_length=100, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='composer',
            name='description_ko',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='composer',
            name='name_ko',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='composer',
            name='placeOfBirth_ko',
            field=models.CharField(max_length=100, null=True, verbose_name='Место_рождения'),
        ),
        migrations.AddField(
            model_name='composer',
            name='placeOfDeath_ko',
            field=models.CharField(max_length=100, null=True, verbose_name='Место_смерти'),
        ),
        migrations.AddField(
            model_name='era',
            name='description_ko',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='era',
            name='name_ko',
            field=models.CharField(max_length=150, null=True, verbose_name='Эпоха'),
        ),
        migrations.AddField(
            model_name='genre',
            name='description_ko',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='genre',
            name='name_ko',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='performers',
            name='description_ko',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='performers',
            name='name_ko',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='pieceofart',
            name='description_ko',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='pieceofart',
            name='name_ko',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='composer',
            name='dateOfBirth',
            field=models.DateField(default=datetime.date(2022, 6, 8), verbose_name='Дата_рождения'),
        ),
    ]
