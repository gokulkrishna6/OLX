# Generated by Django 4.2.6 on 2023-10-21 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0019_alter_buyerdata_country_alter_buyerdata_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='Product',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='olxApp.productimage'),
        ),
    ]
