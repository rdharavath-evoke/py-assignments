# Generated by Django 2.2 on 2021-12-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0009_certificateofanalysis_po_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='sender_name',
            field=models.CharField(blank=True, db_column='SENDER_NAME', max_length=500, null=True),
        ),
    ]