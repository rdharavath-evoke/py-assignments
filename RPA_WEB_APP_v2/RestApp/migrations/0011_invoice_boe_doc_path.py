# Generated by Django 2.2 on 2021-12-30 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0010_invoice_sender_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='boe_doc_path',
            field=models.TextField(blank=True, db_column='BOE_DOC_PATH', null=True),
        ),
    ]