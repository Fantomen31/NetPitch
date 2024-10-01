# Generated by Django 4.2.16 on 2024-10-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netpitch', '0004_auto_20240927_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborationrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], default='Pending', max_length=10),
        ),
    ]
