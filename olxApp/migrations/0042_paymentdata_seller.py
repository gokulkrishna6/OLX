# Generated by Django 4.2.6 on 2023-11-22 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0041_chatmessage_buyer_chatmessage_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdata',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='olxApp.sellerdata'),
        ),
    ]
