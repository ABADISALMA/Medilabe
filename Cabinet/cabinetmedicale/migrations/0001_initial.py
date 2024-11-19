# Generated by Django 5.0.6 on 2024-05-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('spec', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
            ],
        ),
    ]
