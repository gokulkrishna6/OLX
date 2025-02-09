# Generated by Django 4.2.3 on 2023-09-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olxApp', '0006_productmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Img1', models.ImageField(null=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Img_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Img2', models.ImageField(null=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Img_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Img3', models.ImageField(null=True, upload_to='image/')),
            ],
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='Product_Img1',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='Product_Img2',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='Product_Img3',
        ),
    ]
