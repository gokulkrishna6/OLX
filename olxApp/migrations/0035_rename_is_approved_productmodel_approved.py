# Generated by Django 4.2.6 on 2023-11-16 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0034_productmodel_is_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='is_approved',
            new_name='approved',
        ),
    ]
