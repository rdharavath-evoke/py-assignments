# Generated by Django 2.2 on 2022-01-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0013_invoice_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='comment',
        ),
        migrations.AddField(
            model_name='invoice',
            name='bot_comments',
            field=models.CharField(blank=True, db_column='BOT COMMENTS', max_length=500, null=True),
        ),
    ]
