# Generated by Django 3.2.9 on 2022-03-11 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0003_auto_20220311_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='colleges',
            name='ScholarshipName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
