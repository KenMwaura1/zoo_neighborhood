# Generated by Django 3.2.8 on 2021-11-01 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('z_neighborhood', '0005_alter_neighborhood_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='z_neighborhood.neighborhood'),
        ),
    ]
