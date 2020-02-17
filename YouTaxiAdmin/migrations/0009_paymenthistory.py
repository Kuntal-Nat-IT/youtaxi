# Generated by Django 2.2 on 2020-02-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouTaxiAdmin', '0008_merge_20200213_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('phoneNo', models.TextField()),
                ('amountReceivable', models.FloatField()),
                ('amountReceived', models.FloatField()),
                ('dueAmount', models.FloatField()),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
    ]