# Generated by Django 3.0.2 on 2020-02-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
