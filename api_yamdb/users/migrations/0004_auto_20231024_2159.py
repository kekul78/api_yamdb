# Generated by Django 3.2 on 2023-10-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]