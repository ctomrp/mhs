# Generated by Django 4.2.8 on 2023-12-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientquestionnaire',
            name='evaluation_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Evaluation date'),
        ),
    ]
