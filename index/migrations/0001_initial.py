# Generated by Django 4.0.3 on 2022-03-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cerrajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('desempleado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Futbolista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('desempleado', models.BooleanField()),
                ('club_ftubol', models.CharField(max_length=50)),
            ],
        ),
    ]
