# Generated by Django 2.0 on 2017-12-06 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nataMaps', '0004_auto_20171204_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dieselpm',
            name='total_conc',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='tractpoint',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='tractpoint',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]
