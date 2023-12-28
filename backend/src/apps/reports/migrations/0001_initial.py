# Generated by Django 4.2.8 on 2023-12-28 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyReportIntersex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_report', models.DateField(auto_now_add=True, verbose_name='Date report')),
                ('from_0_to_4', models.IntegerField(null=True, verbose_name='0 to 4')),
                ('from_5_to_9', models.IntegerField(null=True, verbose_name='5 to 9')),
                ('from_10_to_14', models.IntegerField(null=True, verbose_name='10 to 14')),
                ('from_15_to_19', models.IntegerField(null=True, verbose_name='15 to 19')),
                ('from_20_to_24', models.IntegerField(null=True, verbose_name='20 to 24')),
                ('from_25_to_29', models.IntegerField(null=True, verbose_name='25 to 29')),
                ('from_30_to_34', models.IntegerField(null=True, verbose_name='30 to 34')),
                ('from_35_to_39', models.IntegerField(null=True, verbose_name='35 to 39')),
                ('from_40_to_44', models.IntegerField(null=True, verbose_name='40 to 44')),
                ('from_45_to_49', models.IntegerField(null=True, verbose_name='45 to 49')),
                ('from_50_to_54', models.IntegerField(null=True, verbose_name='50 to 54')),
                ('from_55_to_59', models.IntegerField(null=True, verbose_name='55 to 59')),
                ('from_60_to_64', models.IntegerField(null=True, verbose_name='60 to 64')),
                ('from_65_to_69', models.IntegerField(null=True, verbose_name='65 to 69')),
                ('from_70_to_74', models.IntegerField(null=True, verbose_name='70 to 74')),
                ('from_75_to_79', models.IntegerField(null=True, verbose_name='75 to 79')),
                ('more_than_80', models.IntegerField(null=True, verbose_name='More than 80')),
                ('pregnants', models.IntegerField(null=True, verbose_name='Pregnants')),
                ('has_child_under_5', models.IntegerField(null=True, verbose_name='Has child under 5 years old')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyReportMen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_report', models.DateField(auto_now_add=True, verbose_name='Date report')),
                ('from_0_to_4', models.IntegerField(null=True, verbose_name='0 to 4')),
                ('from_5_to_9', models.IntegerField(null=True, verbose_name='5 to 9')),
                ('from_10_to_14', models.IntegerField(null=True, verbose_name='10 to 14')),
                ('from_15_to_19', models.IntegerField(null=True, verbose_name='15 to 19')),
                ('from_20_to_24', models.IntegerField(null=True, verbose_name='20 to 24')),
                ('from_25_to_29', models.IntegerField(null=True, verbose_name='25 to 29')),
                ('from_30_to_34', models.IntegerField(null=True, verbose_name='30 to 34')),
                ('from_35_to_39', models.IntegerField(null=True, verbose_name='35 to 39')),
                ('from_40_to_44', models.IntegerField(null=True, verbose_name='40 to 44')),
                ('from_45_to_49', models.IntegerField(null=True, verbose_name='45 to 49')),
                ('from_50_to_54', models.IntegerField(null=True, verbose_name='50 to 54')),
                ('from_55_to_59', models.IntegerField(null=True, verbose_name='55 to 59')),
                ('from_60_to_64', models.IntegerField(null=True, verbose_name='60 to 64')),
                ('from_65_to_69', models.IntegerField(null=True, verbose_name='65 to 69')),
                ('from_70_to_74', models.IntegerField(null=True, verbose_name='70 to 74')),
                ('from_75_to_79', models.IntegerField(null=True, verbose_name='75 to 79')),
                ('more_than_80', models.IntegerField(null=True, verbose_name='More than 80')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyReportWomen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_report', models.DateField(auto_now_add=True, verbose_name='Date report')),
                ('from_0_to_4', models.IntegerField(null=True, verbose_name='0 to 4')),
                ('from_5_to_9', models.IntegerField(null=True, verbose_name='5 to 9')),
                ('from_10_to_14', models.IntegerField(null=True, verbose_name='10 to 14')),
                ('from_15_to_19', models.IntegerField(null=True, verbose_name='15 to 19')),
                ('from_20_to_24', models.IntegerField(null=True, verbose_name='20 to 24')),
                ('from_25_to_29', models.IntegerField(null=True, verbose_name='25 to 29')),
                ('from_30_to_34', models.IntegerField(null=True, verbose_name='30 to 34')),
                ('from_35_to_39', models.IntegerField(null=True, verbose_name='35 to 39')),
                ('from_40_to_44', models.IntegerField(null=True, verbose_name='40 to 44')),
                ('from_45_to_49', models.IntegerField(null=True, verbose_name='45 to 49')),
                ('from_50_to_54', models.IntegerField(null=True, verbose_name='50 to 54')),
                ('from_55_to_59', models.IntegerField(null=True, verbose_name='55 to 59')),
                ('from_60_to_64', models.IntegerField(null=True, verbose_name='60 to 64')),
                ('from_65_to_69', models.IntegerField(null=True, verbose_name='65 to 69')),
                ('from_70_to_74', models.IntegerField(null=True, verbose_name='70 to 74')),
                ('from_75_to_79', models.IntegerField(null=True, verbose_name='75 to 79')),
                ('more_than_80', models.IntegerField(null=True, verbose_name='More than 80')),
                ('pregnants', models.IntegerField(null=True, verbose_name='Pregnants')),
                ('has_child_under_5', models.IntegerField(null=True, verbose_name='Has child under 5 years old')),
            ],
        ),
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_report', models.DateField(auto_now_add=True, verbose_name='Date report')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient', verbose_name='Patient')),
            ],
        ),
    ]