# Generated by Django 2.2 on 2022-01-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0012_invoice_sender_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='comment',
            field=models.CharField(blank=True, db_column='COMMENT', max_length=500, null=True),
        ),
    ]
