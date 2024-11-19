# Generated by Django 5.0.6 on 2024-05-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinetmedicale', '0006_patient_alter_appointment_id_alter_signup_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id_sign_up',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]