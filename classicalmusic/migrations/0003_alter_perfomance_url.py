# Generated by Django 4.0.4 on 2022-05-30 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classicalmusic', '0002_pieceofart_photo_alter_composer_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfomance',
            name='url',
            field=models.SlugField(max_length=300, unique=True),
        ),
    ]
