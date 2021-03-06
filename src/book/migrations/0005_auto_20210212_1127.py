# Generated by Django 2.2.7 on 2021-02-12 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_genre_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='Author',
            field=models.ForeignKey(default='default_title', on_delete=django.db.models.deletion.PROTECT, related_name='genres', to='book.Author', verbose_name='Author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='book_name',
            field=models.CharField(max_length=50, verbose_name='Book name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Author name'),
        ),
    ]
