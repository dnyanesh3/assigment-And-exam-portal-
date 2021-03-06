# Generated by Django 3.0.3 on 2020-07-09 17:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0003_file_question'),
        ('assignment', '0002_remove_fileupload_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentsLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Assignment')),
                ('result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.MCQResult')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
