# Generated by Django 5.0.5 on 2024-05-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0004_quote_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.TextField(default=''),
        ),
    ]
