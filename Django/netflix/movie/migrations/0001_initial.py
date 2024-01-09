# Generated by Django 4.2.6 on 2024-01-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('release_date', models.DateField()),
                ('in_theater', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=5)),
                ('rating', models.FloatField()),
                ('language', models.CharField(choices=[('hindi', 'Hindi'), ('marathi', 'Marathi'), ('english', 'English')], max_length=15)),
            ],
        ),
    ]
