# Generated by Django 4.2.3 on 2023-07-31 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=435, max_length=128),
            preserve_default=False,
        ),
    ]