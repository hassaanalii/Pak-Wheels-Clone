# Generated by Django 4.2.4 on 2023-10-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_favorite_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
