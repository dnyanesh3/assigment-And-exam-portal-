# Generated by Django 3.0.3 on 2020-07-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_notificationforstudent_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationforstudent',
            name='slug',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
