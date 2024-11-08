# Generated by Django 5.1.1 on 2024-10-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('not specified', 'not specified')], default='not specified', max_length=25)),
            ],
        ),
    ]