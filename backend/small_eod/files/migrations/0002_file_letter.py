# Generated by Django 3.0.1 on 2020-01-09 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('letters', '0001_initial'),
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='letter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letters.Letter'),
        ),
    ]
