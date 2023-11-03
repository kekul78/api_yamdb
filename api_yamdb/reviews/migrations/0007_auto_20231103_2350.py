# Generated by Django 3.2 on 2023-11-03 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_comment_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'default_related_name': 'comments', 'ordering': ('pub_date',), 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'default_related_name': 'reviews', 'ordering': ('pub_date',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]