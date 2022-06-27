# Generated by Django 3.2.2 on 2022-06-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce', '0012_delete_purchaseorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('qty_comic', models.IntegerField()),
            ],
        ),
    ]