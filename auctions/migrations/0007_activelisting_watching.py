# Generated by Django 3.2.3 on 2021-07-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210703_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='activelisting',
            name='watching',
            field=models.CharField(default='Add to watchlist', max_length=50),
        ),
    ]
