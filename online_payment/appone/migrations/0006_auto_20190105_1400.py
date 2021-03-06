# Generated by Django 2.1.1 on 2019-01-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0005_auto_20190103_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='accountinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='paidCurrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billno', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('paid_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='unpaidCurrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billno', models.IntegerField()),
                ('month', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='currentbill',
            name='userid',
            field=models.IntegerField(),
        ),
    ]
