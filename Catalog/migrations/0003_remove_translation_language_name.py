# Generated by Django 3.1.1 on 2020-09-18 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0002_auto_20200918_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translation',
            name='language_name',
        ),
    ]