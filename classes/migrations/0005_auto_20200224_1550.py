# Generated by Django 2.1.5 on 2020-02-24 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20200224_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
