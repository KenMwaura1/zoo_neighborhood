# Generated by Django 3.2.8 on 2021-11-01 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('z_neighborhood', '0004_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='admin',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='z_neighborhood.userprofile'),
        ),
    ]
