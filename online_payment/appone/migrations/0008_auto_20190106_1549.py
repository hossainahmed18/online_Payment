# Generated by Django 2.1.1 on 2019-01-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0007_accountinfo_account_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='userid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='currentbill',
            name='userid',
            field=models.IntegerField(default=0),
        ),
    ]