# Generated by Django 3.2.4 on 2021-06-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
