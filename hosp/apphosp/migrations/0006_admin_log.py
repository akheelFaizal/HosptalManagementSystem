# Generated by Django 5.1.1 on 2024-10-18 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphosp', '0005_appointments_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adName', models.CharField(max_length=200)),
                ('adPass', models.CharField(max_length=200)),
            ],
        ),
    ]
