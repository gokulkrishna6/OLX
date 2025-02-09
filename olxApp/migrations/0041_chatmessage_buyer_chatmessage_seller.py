# Generated by Django 4.2.6 on 2023-11-22 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0040_reviewdata_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='olxApp.buyerdata'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='olxApp.sellerdata'),
        ),
    ]
