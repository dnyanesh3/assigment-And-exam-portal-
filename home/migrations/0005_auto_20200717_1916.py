# Generated by Django 3.0.3 on 2020-07-17 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200717_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Class'),
        ),
    ]
