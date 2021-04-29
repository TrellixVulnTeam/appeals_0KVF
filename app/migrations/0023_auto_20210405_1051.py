# Generated by Django 3.0 on 2021-04-05 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20210330_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criticaldatesmaster',
            name='progress',
            field=models.CharField(blank=True, choices=[('Not Applicable', 'Not Applicable'), ('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Not Started', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tblappealmaster',
            name='appealStructure',
            field=models.CharField(blank=True, choices=[('CIRP', 'CIRP'), ('Optional', 'Optional'), ('Individual', 'Individual')], db_column='appealStructure', max_length=25, null=True),
        ),
    ]
