# Generated by Django 3.0.1 on 2020-01-09 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institutions', '0002_auto_20200109_1348'),
        ('letters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='letter_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='letter',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='institutions.Institution'),
        ),
        migrations.AddField(
            model_name='letter',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='letter_modified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='description',
            name='letter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letters.Letter'),
        ),
    ]
