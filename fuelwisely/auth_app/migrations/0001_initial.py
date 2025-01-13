# Generated by Django 5.1.4 on 2025-01-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
