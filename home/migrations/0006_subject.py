# Generated by Django 3.0.3 on 2020-07-18 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200717_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Class')),
            ],
        ),
    ]
