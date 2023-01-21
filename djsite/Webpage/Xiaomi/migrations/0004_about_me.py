# Generated by Django 4.1.3 on 2023-01-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Xiaomi', '0003_laptops'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
