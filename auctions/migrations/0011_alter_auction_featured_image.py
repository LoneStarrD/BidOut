# Generated by Django 4.1.7 on 2023-03-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auction_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]