# Generated by Django 3.1.7 on 2021-04-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdb', '0008_auto_20210318_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='has_annotations',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
