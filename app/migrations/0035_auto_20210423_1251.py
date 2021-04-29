# Generated by Django 3.0 on 2021-04-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20210423_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblappealmaster',
            name='appealStructure',
            field=models.CharField(blank=True, choices=[('Optional', 'Optional'), ('Individual', 'Individual'), ('CIRP', 'CIRP')], db_column='appealStructure', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='tblprovidermaster',
            name='provMasterDeterminationType',
            field=models.CharField(blank=True, choices=[('RNPR', 'RNPR'), ('FR', 'FR'), ('NPR', 'NPR')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='tblprovidermaster',
            name='provMasterIsActive',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
