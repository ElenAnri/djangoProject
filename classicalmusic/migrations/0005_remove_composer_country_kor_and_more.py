# Generated by Django 4.0.4 on 2022-05-30 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classicalmusic', '0004_composer_country_en_composer_country_kor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composer',
            name='country_kor',
        ),
        migrations.RemoveField(
            model_name='composer',
            name='description_kor',
        ),
        migrations.RemoveField(
            model_name='composer',
            name='name_kor',
        ),
        migrations.RemoveField(
            model_name='composer',
            name='placeOfBirth_kor',
        ),
        migrations.RemoveField(
            model_name='composer',
            name='placeOfDeath_kor',
        ),
        migrations.RemoveField(
            model_name='era',
            name='description_kor',
        ),
        migrations.RemoveField(
            model_name='era',
            name='name_kor',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='description_kor',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name_kor',
        ),
        migrations.RemoveField(
            model_name='performers',
            name='description_kor',
        ),
        migrations.RemoveField(
            model_name='performers',
            name='name_kor',
        ),
        migrations.RemoveField(
            model_name='pieceofart',
            name='description_kor',
        ),
        migrations.RemoveField(
            model_name='pieceofart',
            name='name_kor',
        ),
    ]
