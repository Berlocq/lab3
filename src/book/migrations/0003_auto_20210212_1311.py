# Generated by Django 3.1.6 on 2021-02-12 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210212_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Book name'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='genres', to='book.author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, max_length=100, verbose_name='book description'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='style',
            field=models.CharField(blank=True, max_length=50, verbose_name='style book'),
        ),
    ]
