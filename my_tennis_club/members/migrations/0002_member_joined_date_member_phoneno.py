# Generated by Django 4.2.1 on 2023-05-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phoneno',
            field=models.IntegerField(null=True),
        ),
    ]
