# Generated by Django 3.0.3 on 2020-07-17 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200717_1916'),
        ('assignment', '0004_auto_20200717_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='ass_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Class'),
        ),
    ]
