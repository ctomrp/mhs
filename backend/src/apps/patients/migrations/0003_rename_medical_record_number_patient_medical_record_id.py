# Generated by Django 4.2.8 on 2023-12-25 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_alter_patient_diagnostics_alter_patient_groups'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='medical_record_number',
            new_name='medical_record_id',
        ),
    ]