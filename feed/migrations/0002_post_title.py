# Generated by Django 3.2.4 on 2021-06-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=True, max_length=30),
        ),
    ]