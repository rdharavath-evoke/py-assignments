# Generated by Django 2.2 on 2022-01-28 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=6)),
                ('Vendor', models.CharField(max_length=200)),
                ('Base_Code', models.CharField(max_length=200)),
                ('COA_Charecteristic', models.CharField(max_length=200)),
                ('COA_UNIT', models.CharField(max_length=200)),
                ('COA_Specification', models.CharField(max_length=200)),
                ('SAP_Group', models.CharField(max_length=200)),
                ('SAP_Group_Counter', models.CharField(max_length=200)),
                ('SAP_Charecteristic', models.CharField(max_length=200)),
                ('SAP_accepted_result', models.CharField(max_length=200)),
                ('SAP_rejected_result', models.CharField(max_length=200)),
                ('Material', models.CharField(max_length=200)),
                ('Material_Description', models.CharField(max_length=200)),
                ('Change_Log', models.CharField(max_length=200)),
                ('Version', models.CharField(max_length=200)),
            ],
        ),
    ]
