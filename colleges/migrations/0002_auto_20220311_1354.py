# Generated by Django 3.2.9 on 2022-03-11 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colleges',
            name='MaximumSAT',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='colleges',
            name='MinimumSAT',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
