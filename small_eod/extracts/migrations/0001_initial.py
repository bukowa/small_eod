# Generated by Django 2.0.5 on 2018-06-29 00:46

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('subject', models.TextField()),
                ('from_address', models.TextField()),
                ('body', models.TextField()),
                ('attachments_count', models.TextField()),
                ('date', models.TextField()),
            ],
            options={
                'verbose_name': 'Mails',
                'verbose_name_plural': 'Mails',
            },
        ),
    ]
