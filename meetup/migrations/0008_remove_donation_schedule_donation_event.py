# Generated by Django 4.2.2 on 2023-06-25 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0007_alter_guest_telegram_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='schedule',
        ),
        migrations.AddField(
            model_name='donation',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations', to='meetup.event', verbose_name='Событие'),
        ),
    ]
