# Generated by Django 4.2.2 on 2023-06-22 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='speaker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='schedules', to='meetup.guest', verbose_name='Спикер'),
        ),
    ]
