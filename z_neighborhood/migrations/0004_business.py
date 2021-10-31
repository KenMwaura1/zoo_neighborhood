# Generated by Django 3.2.8 on 2021-10-31 21:54

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('z_neighborhood', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('business_logo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='z_neighborhood.neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='z_neighborhood.userprofile')),
            ],
        ),
    ]