# Generated by Django 5.1.1 on 2024-10-28 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apphosp', '0006_admin_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='bk_status',
            field=models.CharField(choices=[('approve', 'approve'), ('reject', 'reject'), ('pending', 'pending')], default='pending', max_length=25),
        ),
    ]