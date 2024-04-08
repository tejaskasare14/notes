# Generated by Django 4.2.6 on 2024-04-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('designation', models.CharField(choices=[('hr', 'HR'), ('manager', 'MANAGER'), ('trainer', 'TRAINER')], max_length=30)),
            ],
        ),
    ]