# Generated by Django 4.1.1 on 2022-12-31 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carprice',
            name='carbody',
            field=models.CharField(default='hello', max_length=50),
            preserve_default=False,
        ),
    ]
