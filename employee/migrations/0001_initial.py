# Generated by Django 3.1.4 on 2020-12-15 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import employee.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('employee_id', models.PositiveIntegerField()),
                ('city', models.CharField(max_length=50)),
                ('media_file', models.FileField(default='', upload_to='uploads/', validators=[employee.validator.validate_file_size])),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
