# Generated by Django 2.0 on 2017-12-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dieselPM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_conc', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Tract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateFP', models.IntegerField()),
                ('stateName', models.CharField(max_length=16, null=True)),
                ('countyFP', models.IntegerField()),
                ('geoid', models.IntegerField()),
                ('population', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TractPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=3, max_digits=8)),
                ('lng', models.DecimalField(decimal_places=3, max_digits=8)),
                ('tract', models.ForeignKey(on_delete='cascade', to='nataMaps.Tract')),
            ],
        ),
        migrations.AddField(
            model_name='dieselpm',
            name='tract',
            field=models.ForeignKey(on_delete='cascade', to='nataMaps.Tract'),
        ),
    ]
