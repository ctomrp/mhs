# Generated by Django 4.2.8 on 2023-12-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectors', '0002_alter_sector_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(default=None, max_length=255, unique=True, verbose_name='Sector'),
        ),
    ]