# Generated by Django 2.0 on 2017-12-04 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nataMaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tractpoint',
            name='lat',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tractpoint',
            name='lng',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
