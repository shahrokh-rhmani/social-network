# Generated by Django 3.2.5 on 2022-06-27 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jwitter', '0002_jweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Jweets', to=settings.AUTH_USER_MODEL),
        ),
    ]